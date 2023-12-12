# coniferous-caroler
 The Coniferous Caroler is an Internet-connected holiday decoration that senses when you walk within range, queues songs for you and puts on a light show to them. This repository contains the software stack to run the Coniferous Caroler.

## Prerequisites
 For this software to function, you need the appropriate hardware and the following packages installed/compiled:
 - pydbus
 - Spotifyd
 - PulseAudio
 - CAVA
 - CircuitPython
 - Adafruit NeoPixel

## Instructions
 To run the scripts, execute the following commands in order:
 - "sudo ./spotifyd --no-daemon --pulseaudio"
 - "sudo python3 spotipy_speaker_control.py"
 - "sudo python3 light-show.py"

## Miscellaneous
 Additional scripts are included in this repository for use in the main scripts and testing hardware components.
