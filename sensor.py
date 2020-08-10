# coding: UTF-8


import os
import glob
from time import sleep

class DS18B20_sensor:
    
    def __init__(self, base_dir, device_file):
        self.dir = base_dir
        self.folder = glob.glob(base_dir + '28*')[0]
        self.file = self.folder + device_file
        self.temp_c = None
    
    def read_temp_raw(self):
        f = open(self.file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            sleep(0.2)
            lines = self.read_temp_raw()
        # 読み込んだファイルの中から温度の部分を抜き出す
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            self.temp_c = float(temp_string) / 1000.0
            return self.temp_c
