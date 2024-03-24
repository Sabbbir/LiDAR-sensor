import serial
import re
import time
# Collecting data from LiDAR sensor
def parse_data(data):
    data_str = data.decode('utf-8')  # Convert bytes to string
    # Extract distance and strength values using regular expressions
    match_distance = re.search(r'(\d+)cm', data_str)
    match_strength = re.search(r'strength: (\d+)', data_str)
    if match_distance and match_strength:
        distance = int(match_distance.group(1))
        strength = int(match_strength.group(1))
        return distance, strength
    else:
        return None, None


Arduino = serial.Serial("/dev/ttyACM0")


# Reading data from LiDAR sensor
def read_data():
    if Arduino.in_waiting > 0:
        myData = Arduino.readline()
        distance, strength = parse_data(myData)
        return distance, strength
    else:
        return None, None


def data():
    if Arduino.in_waiting > 0:
        myData = Arduino.readline()
        distance, strength = parse_data(myData)
    while True:
        distance, strength = read_data()
        if distance is not None and strength is not None:
            print(f"Dist: {distance}cm\t Strength: {strength}")
        time.sleep(.1)


def detection():
    if Arduino.in_waiting > 0:
        myData = Arduino.readline()
        distance, strength = parse_data(myData)
        while True:
            distance, strength = read_data()
            if distance is not None and strength is not None:
                if distance < 500 and strength > 500:
                    return True
                    # print("True", " ", distance, " ", strength)
                else:
                    return False
                    # print("False", " ", distance, " ", strength)
            time.sleep(.1)



