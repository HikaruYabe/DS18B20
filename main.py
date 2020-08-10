# coding: UTF-8

import sensor
from time import sleep


def main():
    sensor_0 = sensor.DS18B20_sensor('/sys/bus/w1/devices/','/w1_slave')
    try:
        while True:
            print(sensor_0.read_temp())
            sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()