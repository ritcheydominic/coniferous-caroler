import time
import board
import neopixel

LED_PIN = board.D21
NUM_LEDS = 100
LED_ORDER = neopixel.RGB

led_strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=0.5, auto_write=False, pixel_order=LED_ORDER)

while True:
    for i in range(NUM_LEDS):
        led_strip.fill((0, 0, 0))
        led_strip[i] = (255, 0, 0)
        time.sleep(1)