#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import json

dict = {}
index = 1

# def main():
    s = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)
    print s.portstr
    for num in range(300):
        val = s.readline(30)
        dict[index] = int(val)
        index += 1

f = open('data.json', 'w')
json.dump(dict, f, indent=4, sort_keys=True)

# if __name__ == '__main__':
#     main()
