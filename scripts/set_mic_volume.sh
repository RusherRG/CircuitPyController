#!/bin/bash

echo "Set microphone volume to $1"
pactl set-source-volume 0 $1%
