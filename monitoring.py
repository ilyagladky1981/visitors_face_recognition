import face_recognition
from PIL import Image, ImageDraw
import pickle
import os
import cv2

# Const

camers_for_monitoring = dict(new6:[13,14,15,16], new3:[14], new2:[12, 13, 16], new1:[15], 4k2:[21])
registrator_ip_port = {new1:'', new2:'', new3:'', new6:'', reg_4k2:''}

# Functions



def main():
    # Программа мониторинга лиц посетителей
    for key in camers_for_monitoring.keys():
    print "%s -> %s" % (key, camers_for_monitoring[key])
    # camera_number = 1
    # camera_obj = create_camera(str(cam_no))
    # while True:
    #    ret, current_frame = cam.read()
    #    dim = (width, height)
    #    Full_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA)


if __name__ == '__main__':
    main()




