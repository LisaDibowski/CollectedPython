import time
from rpi_ws281x import PixelStrip, Color
from w1thermsensor import W1ThermSensor
import argparse
import neopixel
import board

pixel_pin = board.D18
num_pixels = 64


# LED_COUNT = 16        # Number of LED pixels.
# LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
# LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA = 10          # DMA channel to use for generating signal (try 10)
# LED_BRIGHTNESS = 126  # Set to 0 for darkest and 255 for brightest
# LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
# LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Modify these values for each sensor
namespace = "Temperature Sensors for LEDs"
location = "RZX"
sensor_names = {"28-011453D008AA": "NR1", "28-011453D2EDAA": "NR2", "28-011453CFAAAA": "NR3", "28-3C01A816DECF": "NR4", "28-011453CA1FAA": "NR5", "28-011453E9E1AA": "NR6"}

metrics = []
for sensor in W1ThermSensor.get_available_sensors():
    print(
        'Sensor "%s" has temperature %.2f'
        % (sensor_names[sensor.id], sensor.get_temperature())
    )
    metrics.append(
        {
            "MetricName": "Temperature",
            "Dimensions": [
                {"Name": "Location", "Value": location},
                {"Name": "Placement", "Value": sensor_names[sensor.id]},
            ],
            "Unit": "None",
            "Value": sensor.get_temperature(),
        }
    )

# Sensor D008AA

sens1 = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="28-011453D008AA")
temperature_in_celsius = sens1.get_temperature()

def calcAllAverages():
    area1=calcAverage(sens1, sens2)
    area2=calcAverage(sens3, sens4)
    area3=calcAverage(sens5, sens6)

def calcAverage(sens1, sens2):
    return ((sens1+sens2)/2)

def calcAverage(sens3, sens4):
    return ((sens1+sens2)/2)


# Color Wipe to reset everything 
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Color Test basic
def basicRed(strip, color, wait_ms=50):
    if 
