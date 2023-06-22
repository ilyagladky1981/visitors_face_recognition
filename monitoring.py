import face_recognition
from PIL import Image, ImageDraw
import pickle
import os
import cv2

# Const

cameras_for_monitoring = {'new6':[13,14,15,16], 'new3':[14], 'new2':[12, 13, 16], 'new1':[15], '4k2':[21]}
registrator_ip_port = {'new1':'192.168.11.243:554', 'new2':'192.168.11.158:554', 'new3':'192.168.11.140:554', 'new6':'192.168.11.53:554', '4k2':'192.168.1.3:554'}
rtsp_username = 'admin'
rtsp_password = ''
width = 1920
height = 1080

# Functions


def create_capture(current_registrator_ip_port, channel):
    rtsp = f"rtsp://" + current_registrator_ip_port + \
          "/user={rtsp_username}" + \
          "&password={rtsp_password}" + \
          "&channel={channel}"  + \
          "&stream=0.sdp"
    capture = cv2.VideoCapture()
    capture.open(rtsp)
    return capture



def main():
    # Программа мониторинга лиц посетителей
    registrator_id = cameras_for_monitoring.keys[0]
    camera_number = cameras_for_monitoring[registrator_id][0]
    current_registrator_ip_port = registrator_ip_port[registrator_id]
    capture_obj = create_capture(current_registrator_ip_port, str(camera_number))
    file_count = 0
    while(capture_obj.isOpened()):
        file_count += 1
        ret, current_frame = capture_obj.read()
        if ret == True:
          writefile = f"Resources/Image_sequence/cam{camera_number}_{file_count}.jpg"
          capture_obj.imwrite(writefile, frame)
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




