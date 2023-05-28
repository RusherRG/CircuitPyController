#!/bin/bash

echo "Set volume to $1%"
pactl set-sink-volume 0 $1%
