#!/usr/bin/env python3
import time
from rpi_ws281x import PixelStrip, Color
from w1thermsensor import W1ThermSensor
import argparse
import neopixel
import board


# LED strip configuration:
LED_COUNT = 130        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Sensor 28-011453D008AA

sens1 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-011453D008AA")
temperature_in_celsius = sens1.get_temperature()

# Sensor 28-011453D2EDAA

sens2 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-011453D2EDAA")
temperature_in_celsius = sens2.get_temperature()

# Sensor 28-011453CFAAAA

sens3 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-011453CFAAAA")
temperature_in_celsius = sens3.get_temperature()

# Sensor 28-3C01A816DECF

sens4 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-3C01A816DECF")
temperature_in_celsius = sens4.get_temperature()

# Sensor 28-011453CA1FAA

sens5 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-011453CA1FAA")
temperature_in_celsius = sens5.get_temperature()

# Sensor 28-011453E9E1AA

sens6 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-011453E9E1AA")
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


RANGE1 = range(0,44)
RANGE2 = range(44,80)
RANGE3 = range(80,NUM_LEDS)

def setStrip1(color):
    for i in range(RANGE1):
        strip.setPixelColor(i, color)
    strip.show()

def setStrip2(color):
    for i in range(RANGE2):
        strip.setPixelColor(i, color)
    strip.show()

def setStrip3(color):
    for i in range(RANGE3):
        strip.setPixelColor(i, color)
    strip.show()



colors = [
  (40, (255, 0, 0)), 
  (37, (255, 67, 30)),
  (34, (228, 96, 94)),
  (31, (255, 117, 20)),
  (28, (255, 196, 20)),
  (25, (45, 230, 88)),
  (22, (124, 211, 122)),
  (19, (11, 255, 205)),
  (16, (0, 255, 255)),
  (13, (47, 170, 255)),
  (10, (0, 0, 255))
]
DEFAULTTEMP = (255,255,255) # default color

def temperatureColor(temperature):
  for temp, color in colors:
    if temperature <= temp:
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
            time.sleep(DELAY) # don't update too often


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
