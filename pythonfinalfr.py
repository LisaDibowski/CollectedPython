import time
from rpi_ws281x import PixelStrip, Color
from w1thermsensor import W1ThermSensor
import argparse
import neopixel
import board

# pixel_pin = board.D18
# num_pixels = 64


# LED strip configuration:
LED_COUNT = 128        # Number of LED pixels.
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


# def calcAllAverages():
#    area1=calcAverage(sens1, sens2)
#    area2=calcAverage(sens3, sens4)
#    area3=calcAverage(sens5, sens6)

def calcAverage1(sens1, sens2):
    return ((sens1+sens2)/2) 

def calcAverage2(sens3, sens4):
    return ((sens3+sens4)/2)

def calcAverage3(sens5, sens6):
    return ((sens5+sens6)/2)

# beep colors down below

def colorRedHigh():
    return Color(255, 0, 0)

def colorRedMedium():
    return Color(255, 67, 30)

def colorRedLow():
    return Color(228, 96, 94)

def colorYellowHigh():
    return Color(255, 117, 20)

def colorYellowLow():
    return Color(255, 196, 20)

def colorGreenHigh():
    return Color(45, 230, 88)

def colorGreenMedium():
    return Color(124, 211, 122)

def colorGreenLow():
    return Color(11, 255, 205)

def colorBlueHigh():
    return Color(0, 255, 255)

def colorBlueMedium():
    return Color(47, 170, 255)

def colorBlueLow():
    return Color(0, 0, 255)

# beep things that do things beep

# Color Wipe to reset everything 
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# beep we define the area

def ledArea1():
    


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
            




    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
