import serial
import time
import json


def main():
    dict = {}
    index = 1

    s = serial.Serial('/dev/ttyACM1', 9600)
    time.sleep(2)

    print s.portstr

    for num in range(300):
        val = s.readline()
        dict[index] = int(val)
        index += 1

    
    f = open('data.json','w')
    json.dump(dict,f, indent=4, sort_keys=True)
    f.close()

if __name__ == '__main__':
    main()

