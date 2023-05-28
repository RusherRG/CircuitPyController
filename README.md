# CircuitPyController
Use CircuitPY to add a new USB Keyboard. For each keypress, different triggers can be called like running scripts, simulating an actual key press or resetting the keyboard. Even supports potentiometers, as of now it works for input and output volume changes.

# Instructions

Configure the actions for each keypress and potentiometer value changes in `config.py`. Map the pins to the pins on the board.

Run the following on the host machine
```sh
# make sure that the tty is accessible by the user
sudo chmod 666 /dev/ttyACM0
# run the host script that is capable to interact with the host machine
python3 host.py
```