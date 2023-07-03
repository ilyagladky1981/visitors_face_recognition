import face_recognition
from PIL import Image, ImageDraw
import pickle
import os
import cv2
import numpy as np
import sqlite3
from sqlite3 import Error


# Const


FACE_BD = "./DB/face_db.sqlite"
cameras_for_monitoring = {'new6':[15]}
registrator_ip_port = {'new6':'192.168.11.53:554'}
RSTP_USERNAME = 'admin'
RSTP_PASSWORD = ''
WIDTH = 1920
HEIGHT = 1080

# Functions

def camera_capture(current_registrator_ip_port, channel):
    rtsp = f"rtsp://" + current_registrator_ip_port + \
          f"/user={RSTP_USERNAME}" + \
          f"&password={RSTP_PASSWORD}" + \
          f"&channel={channel}"  + \
          f"&stream=0.sdp"
    print("rtsp=",rtsp)
    capture = cv2.VideoCapture()
    capture.open(rtsp)
    #print("capture=",dir(capture))
    return capture

def InitDB(path):
    connection = create_connection(FACE_BD)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    records = cursor.fetchall()
    records = list(records[0])
    print(records)
    print(type(records))
    if not('staff_monitoring' in records):
        sqlite_create_table_query = '''CREATE TABLE staff_monitoring (
            id INTEGER PRIMARY KEY,
            staff_id INTEGER,
            registrator_name TEXT NOT NULL,
            camera_num INTEGER NOT NULL,
            DataTime datetime default current_timestamp);'''
        cursor.execute(sqlite_create_table_query)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    records = list(cursor.fetchall())
    records = list(*records[0])
    print(records)
    print(type(records))
    cursor.close()
    connection.close()


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print("Connection to SQLite DB successful")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def main():
    # Программа мониторинга лиц посетителей
    data = {'encodings':[], 'name':[]}
    registrators = list(cameras_for_monitoring.keys())
    registrator_id = registrators[0]
    camera_number = cameras_for_monitoring[registrator_id][0]
    current_registrator_ip_port = registrator_ip_port[registrator_id]
    capture_obj = camera_capture(current_registrator_ip_port, str(camera_number))
    count = 0

    InitDB(FACE_BD)

    exit(0)

    connection = create_connection(FACE_BD)
    cursor = connection.cursor()


if __name__ == '__main__':
    main()





