from adafruit_hid.keycode import Keycode

scripts_path = "/media/rusherrg/CIRCUITPY/scripts/"

keys_config = {
    "1": {"name": "healthcheck", "type": "script", "value": "script_1", "switch": None},
    "2": {"name": "KeyPress A", "type": "key_press", "value": Keycode.A, "switch": None},
}

potentiometers_config = [
    {
        "name": "volume_control",
        "value": 0,
        "script": "set_volume.sh",
        "potentiometer": None,
    },
    {
        "name": "mic_control",
        "value": 0,
        "script": "set_mic_volume.sh",
        "potentiometer": None,
    },
]

config = {
    "scripts_path": scripts_path,
    "keys_config": keys_config,
    "potentiometers_config": potentiometers_config,
}
