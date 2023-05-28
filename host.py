import serial
import subprocess


def run_trigger(command):
    command = "/bin/bash " + command
    try:
        result = subprocess.run(command.split(), capture_output=True)
        output = result.stdout.decode()
        print(output)
    except Exception as e:
        print(e)


with serial.Serial("/dev/ttyACM0", 115200, timeout=10) as ser:
    while True:
        try:
            serial_input = ser.readline()
            serial_input = serial_input.decode().strip()
            print(serial_input)
            if serial_input.find("run trigger:") != -1:
                command = serial_input.split("trigger:")[1].strip()
                run_trigger(command)
        except serial.serialutil.SerialException:
            print("error")
