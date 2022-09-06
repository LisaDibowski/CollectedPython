import time
import board
import neopixel
from rpi_ws281x import PixelStrip, Color
import argparse
import math

# Hier wird das Verhalten der LED Strips konfiguriert

LED_COUNT = 70        # Anzahl der angesteuerten LED Pixel 
LED_PIN = 18          # GPIO pin wird definiert. Nach Herstelleranweisung ist das der GPIO18 Pin.
LED_FREQ_HZ = 800000  # LED Signalfrequenz. Entweder 400KHz oder 800KHz. Eventuell muss dieser Wert verringert werden
LED_DMA = 10          # DMA Kanal für das Signal. 10 ist Standard und sollte als erstes probiert werden
LED_BRIGHTNESS = 128  # LED Helligkeit. Dies ist der wichtigste Wert der eventuell weiter geändert werden muss wenn es zu Spannungsproblemen kommt wegen dem Gebrauch von nur einem Netzteil.
LED_INVERT = False    # Kann ignoriert werden. Nur in speziellen Fällen benötigt wenn eine bestimmte Art von level shifter benutzt wird.
LED_CHANNEL = 0       # Auf '1' setzen wenn die GPIOs 13, 19, 41, 45 or 53 benutzt werden sollten



sensorids = ["INSERT ID0", "INSERT ID1", "INSERT ID2", "INSERT ID3", "INSERT ID4", "INSERT ID5", "INSERT ID6", "INSERT ID7"]

temp_very_low
temp_low
temp_mid
temp_high
temp_very_high
temp_dangerous


# temp_color_very_low = (strip, Color(0, 0, 255))
# temp_color_low = (strip, Color(30, 144, 255))
# temp_color_mid = (strip, Color(135, 206, 250))
# temp_color_high = (strip, Color(255,255,0))
# temp_color_very_high = (strip, Color(255, 140, 0))
# temp_color_dangerous_ = (strip, Color(255, 0, 0))

# Hier wird die Funktion definiert mit der später die in device_file spezifizierten Sensoren ausgelesen werden (Im raw Format, das heißt ohne C Konvertierung)

def read_temp_raw():
    f = open(device_file, "r")
    lines = f.readlines()
    f.close()
    return lines

# Hier wird die Funktion definiert mit der die Temperatur die mit read_temp_raw ausgelesen wurde dann in C Konvertiert wird. Das ganze wird dann mit temp_c returned

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        
        return temp_c



# In diesem Loop wird alles zusammengeführt 	
while True:
    data =""
    for sensor in range(len(sensorids)):
        device_file = "/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave"
        temperature = (read_temp())
        dtemp = "%.1f" % temperature
        result = (str(dtemp)) + " C "


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        
        while True:
    data =""
    for sensor in range(len(sensorids)):
        device_file = "/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave"
        temperature = (read_temp())
        dtemp = "%.1f" % temperature
        result = (str(dtemp)) + " C "



        print
