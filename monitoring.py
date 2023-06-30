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
    
    
    #path = os.path.dirname(2.__file__)
    #print("cv2=",path)
    
    while(capture_obj.isOpened()):
        #while(count < 1):
        count += 1
        ret, current_frame = capture_obj.read()
        #print(current_frame.shape)
        #print(current_frame.dtype)
        #print("ret, count=", ret, count)
        if ret == True:
            writefile = f"/home/igladky/m_face_recognition/Data/" + \
                        f"Image_sequence/reg{registrator_id}_" + \
                        f"cam{camera_number}_{count}.jpg"
            # image_directory = os.path.dirname(writefile)
            # print(os.listdir(image_directory))
            # img_cur_frame = Image.fromarray(current_frame)
            # img_cur_frame.save(writefile)
            locations = face_recognition.face_locations(current_frame, model="cnn")
            encodings = face_recognition.face_encodings(current_frame, locations)
            img_count = 0
            for face_encoding, face_location in zip(encodings, locations):
                img_count += 1
                writefile = f"/home/igladky/m_face_recognition/Data/" + \
                            f"Image_sequence/reg{registrator_id}_" + \
                            f"cam{camera_number}_{img_count}.jpg"
                result = face_recognition.compare_faces(data["encodings"], face_encoding)
                match = None
                if True in result:
                    match = data["name"]
                else:
                    # Pillow save image
                    img_cur_frame = Image.fromarray(current_frame)
                    img_cur_frame.save(writefile)
                # Save Name, registrator, camera, Data and Time, and location
                cursor.execute("SELECT * FROM STAFF;")
        k = cv2.waitKey(10)
        if k == ord("q"):
            capture_obj.close()
            cursor.close()
            connection.close()
            print("Q pressed, closing the app")
            break
    pass
    print("dict cameras_for_monitoring")
    #for key in cameras_for_monitoring.keys():
    #    print(f"{key} -> {cameras_for_monitoring[key]}")
    # camera_number = 1
    # camera_obj = create_camera(str(cam_no))
    # while True:
    #    ret, current_frame = cam.read()
    #    dim = (width, height)
    #    Full_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA)


if __name__ == '__main__':
    main()




