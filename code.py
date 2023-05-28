import board
import digitalio
import os
import supervisor
import time
import usb_hid

from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from analogio import AnalogIn

from config import config

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# keys mapping to board
pin_mapping = {
    "1": digitalio.DigitalInOut(board.GP2),
    "2": digitalio.DigitalInOut(board.GP3),
    "3": digitalio.DigitalInOut(board.GP4),
    "4": digitalio.DigitalInOut(board.GP5),
    "5": digitalio.DigitalInOut(board.GP6),
    "6": digitalio.DigitalInOut(board.GP7),
    "7": digitalio.DigitalInOut(board.GP8),
    "8": digitalio.DigitalInOut(board.GP9),
    "9": digitalio.DigitalInOut(board.GP10),
    "10": digitalio.DigitalInOut(board.GP11),
    "11": digitalio.DigitalInOut(board.GP12),
    "12": digitalio.DigitalInOut(board.GP13),
}

# potentiometer connected to A1, power & ground
board_potentiometers = [AnalogIn(board.A0), AnalogIn(board.A1)]
value_step = (2**16) // 20


def load_configs(config):
    switches = config["keys_config"]
    for pin, key_config in switches.items():
        board_pin = pin_mapping[pin]
        board_pin.direction = digitalio.Direction.INPUT
        board_pin.pull = digitalio.Pull.UP
        key_config["switch"] = Debouncer(board_pin)

    potentiometers = config["potentiometers_config"]
    for i in range(len(potentiometers)):
        potentiometers[i]["potentiometer"] = board_potentiometers[i]
        potentiometers[i]["value"] = board_potentiometers[i].value
    return switches, potentiometers


def check_serial_input():
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        return value
    return None


def process_key_presses(switches):
    for pin, config in switches.items():
        switch = config["switch"]
        switch.update()
        if switch.fell:
            print(f"Triggering {config['name']}")
            if config["type"] == "key_press":
                kbd.send(config["value"])
        # if switch.rose:
        #     print(f"{pin} released")
        #     print("was pressed for ", switch.last_duration)


def process_potentiometers(potentiometers):
    for potentiometer in potentiometers:
        if (
            abs(potentiometer["potentiometer"].value - potentiometer["value"])
            >= value_step
        ):
            print(f"Triggering {potentiometer['name']}")
            potentiometer["value"] = potentiometer["potentiometer"].value
            trigger_script_path = config["scripts_path"] + potentiometer["script"]
            trigger_value = ((potentiometer["value"] // value_step) + 1) * 5
            print(f"run trigger: {trigger_script_path} {trigger_value}")


switches, potentiometers = load_configs(config)
print("Switches config")
print(switches)
print("\nPotentiometers config")
print(potentiometers)

while True:
    serial_input = check_serial_input()
    process_key_presses(switches)
    process_potentiometers(potentiometers)
