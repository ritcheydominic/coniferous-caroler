#!/usr/bin/python3
import time
import board
import neopixel
import os
import struct
import subprocess
import tempfile
import colorsys

BARS_NUMBER = 20
# OUTPUT_BIT_FORMAT = "8bit"
OUTPUT_BIT_FORMAT = "16bit"
# RAW_TARGET = "/tmp/cava.fifo"
RAW_TARGET = "/dev/stdout"

LED_PIN = board.D21
NUM_LEDS = 100
LED_ORDER = neopixel.RGB

conpat = """
[general]
bars = %d
[output]
method = raw
raw_target = %s
bit_format = %s
"""

config = conpat % (BARS_NUMBER, RAW_TARGET, OUTPUT_BIT_FORMAT)
bytetype, bytesize, bytenorm = ("H", 2, 65535) if OUTPUT_BIT_FORMAT == "16bit" else ("B", 1, 255)

led_strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=0.35, auto_write=False, pixel_order=LED_ORDER)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def run():
    with tempfile.NamedTemporaryFile() as config_file:
        config_file.write(config.encode())
        config_file.flush()

        process = subprocess.Popen(["cava", "-p", config_file.name], stdout=subprocess.PIPE)
        chunk = bytesize * BARS_NUMBER
        fmt = bytetype * BARS_NUMBER

        if RAW_TARGET != "/dev/stdout":
            if not os.path.exists(RAW_TARGET):
                os.mkfifo(RAW_TARGET)
            source = open(RAW_TARGET, "rb")
        else:
            source = process.stdout
        while True:
            data = source.read(chunk)
            if len(data) < chunk:
                break
            sample_list = [i / bytenorm for i in struct.unpack(fmt, data)]
            avg = 0
            for sample in sample_list:
                avg += sample
            avg /= BARS_NUMBER
            for sample_idx in range(BARS_NUMBER):
                sample = sample_list[sample_idx]
                rgb_color = hsv2rgb(sample, 1.0, avg)
                for idx in range(NUM_LEDS // BARS_NUMBER):
                    led_idx = (sample_idx * (NUM_LEDS // BARS_NUMBER)) + idx
                    led_strip[led_idx] = rgb_color
            led_strip.show()

if __name__ == "__main__":
    try:
        run()
    except:
        led_strip.fill((0, 0, 0))
        led_strip.show()
        os._exit(130)
