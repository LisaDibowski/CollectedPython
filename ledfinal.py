# Importing all the libraries that are being used. 
# Most importantly here is the rpi_ws281x and the w1thermsensor library, 
# which we are gonna be using for most of the important functions

#!/usr/bin/env python3
import time
from rpi_ws281x import PixelStrip, Color
from w1thermsensor import W1ThermSensor, Sensor
import argparse
import neopixel
import board

# This is the part where we can configure the LED Strip itself. 
# LED strip configuration:

LED_COUNT = 82       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# This is an additional ghost variable that we are using for different variations. 
# This one can potentially be phased out.
NUM_LEDS= 82

# In this part of the code we are defining variables for all the sensors that are currently used.
# This can be expanded by simply copying one of the code blocks and replacing sensor_id="xxxxxxxxxxxxxxxx" with whatever sensor ID is in use.
# It is important to remove the "28-" part of the sensor ID

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

# This part is used to take the average of two sensors in order to have usable ranges. 
# Adding more ranges / areas is easily possible by just following the below format.  

def calcAverage1():
    global sens1, sens2
    return ((sens1.get_temperature()+sens2.get_temperature())/2)

def calcAverage2():
    global sens3, sens4
    return ((sens3.get_temperature()+sens4.get_temperature())/2)

def calcAverage3():
    global sens5, sens6
    return ((sens5.get_temperature()+sens6.get_temperature())/2)

# New Function to change the calculations for the ranges.

def calcRange1():
	 global sens1
	 return sens1.get_temperature()

def calcRange1():
	 global sens2
	 return sens2.get_temperature()

def calcRange1():
	 global sens3
	 return sens3.get_temperature()

def calcRange1():
	 global sens4
	 return sens4.get_temperature()

def calcRange1():
	 global sens5
	 return sens5.get_temperature()

def calcRange1():
	 global sens6
	 return sens6.get_temperature()

# Ranges that we use to actually define the areas.
RANGE1 = range(8,30)
RANGE2 = range(30,52)
RANGE3 = range(52,NUM_LEDS)

# Functions that are being used to set the color of the pre-defined ranges.
# time.sleep and wait_ms can be played with for a more responsive experience
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

# Adjust first value to change temperature threshhold, 
# Adjust values after Color to change RGB colors.
# We are here going with a RED (Warmest possible color) to CYAN (Coldest possible color) gradience 
colors = [
  (45, Color(255, 0, 0)),
  (44, Color(255, 26, 0)),
  (43, Color(255, 53, 0)),
  (42, Color(255, 79, 0)),
  (41, Color(255, 106, 0)),
  (40, Color(255, 132, 0)),
  (39, Color(255, 158, 0)),
  (38, Color(255, 185, 0)),
  (37, Color(255, 211, 0)),
  (36, Color(255, 237, 0)),
  (35, Color(246, 255, 0)),
  (34, Color(220, 255, 0)),
  (33, Color(193, 255, 0)),
  (32, Color(167, 255, 0)),
  (31, Color(141, 255, 0)),
  (30, Color(114, 255, 0)),
  (29, Color(88, 255, 0)),
  (28, Color(62, 255, 0)),
  (27, Color(9, 255, 0)),
  (26, Color(0, 255, 18)),
  (25, Color(0, 255, 44)),
  (24, Color(0, 255, 70)),
  (23, Color(0, 255, 97)),
  (22, Color(0, 255, 123)),
  (21, Color(0, 255, 149)),
  (20, Color(0, 255, 176)),
  (19, Color(0, 255, 202)),
  (18, Color(0, 255, 229)),
  (17, Color(0, 255, 255)),
]
# This is the default color that we use as a placeholder variable
DEFAULTTEMP = Color(255,255,255) # default color

# Index Counter function 
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
