#!/usr/bin/env python3
import time
from rpi_ws281x import PixelStrip, Color
from w1thermsensor import W1ThermSensor, Sensor
import argparse
import neopixel
import board


# LED strip configuration:
LED_COUNT = 81       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

NUM_LEDS= 81

# Sensor 28-011453d008aa

sens1 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="011453d008aa")
temperature_in_celsius = sens1.get_temperature()

# Sensor 28-011453d2edaa

sens2 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="011453d2edaa")
temperature_in_celsius = sens2.get_temperature()

# Sensor 28-011453cfaaaa

sens3 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="011453cfaaaa")
temperature_in_celsius = sens3.get_temperature()

# Sensor 28-3c01a816decf

sens4 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="3c01a816decf")
temperature_in_celsius = sens4.get_temperature()

# Sensor 28-011453ca1faa

sens5 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="011453ca1faa")
temperature_in_celsius = sens5.get_temperature()

# Sensor 28-011453e9e1aa

sens6 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="011453e9e1aa")
temperature_in_celsius = sens6.get_temperature()


def calcAverage1():
    global sens1, sens2
    return ((sens1.get_temperature()+sens2.get_temperature())/2)

def calcAverage2():
    global sens3, sens4
    return ((sens3.get_temperature()+sens4.get_temperature())/2)

def calcAverage3():
    global sens5, sens6
    return ((sens5.get_temperature()+sens6.get_temperature())/2)


RANGE1 = range(0,21)
RANGE2 = range(22,43)
RANGE3 = range(44,NUM_LEDS)

def setStrip1(color, wait_ms=50):
    for i in range(RANGE1):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

def setStrip2(color, wait_ms=50):
    for i in range(RANGE2):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

def setStrip3(color, wait_ms=50):
    for i in range(RANGE3):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)


colors = [
  (30, Color(255, 0, 0)),
  (29, Color(255, 78, 0)),
  (28, Color(255, 111, 0)),
  (27, Color(255, 160, 0)),
  (26, Color(255, 200, 0)),
  (25, Color(255, 255, 0)),
  (24, Color(255, 255, 159)),
  (23, Color(99, 255, 170)),
  (22, Color(34, 255, 252)),
  (21, Color(34, 129, 255)),
  (20, Color(0, 0, 255)),
  (19, Color(0, 0, 255)),
  (18, Color(0, 0, 255)),
  (17, Color(0, 0, 255)),
  (16, Color(0, 0, 255)),
  (15, Color(0, 0, 255)),
  (14, Color(0, 0, 255)),
  (13, Color(0, 0, 255)),
  (12, Color(0, 0, 255)),
  (11, Color(0, 0, 255)),
  (10, Color(0, 0, 255)),
]
DEFAULTTEMP = Color(255,255,255) # default color

def temperatureColor(temperature):
  for temp, color in colors:
    if temperature >= temp:
      return color
  return DEFAULTTEMP


# Color Wipe to reset everything 
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)



# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            temperature = calcAverage1()
            print(temperature)
            color = temperatureColor(temperature)
            for pixelNum in RANGE1:
                strip.setPixelColor(pixelNum, color)
            temperature = calcAverage2()
            print(temperature)
            color = temperatureColor(temperature)
            for pixelNum in RANGE2:
                strip.setPixelColor(pixelNum, color)
            temperature = calcAverage3()
            print(temperature)
            color = temperatureColor(temperature)
            for pixelNum in RANGE3:
                strip.setPixelColor(pixelNum, color)
            strip.show()
            time.sleep(50 / 1000.0) # don't update too often


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
