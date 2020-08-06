# coding: UTF-8


import os
import glob
from time import sleep

# ファイルパスを取得
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir +'28*')[0]
device_file = device_folder + '/w1_slave'

# ファイルを開き読み込む
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    # ファイルを開き読み込んだ結果を保存
    lines = read_temp_raw()
    # 温度の取得に成功しているか確認
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()
    # 読み込んだファイルの中から温度の部分を抜き出す
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

try:
    while True:
        print(read_temp())
        sleep(1)
except KeyboardInterrupt:
    pass
