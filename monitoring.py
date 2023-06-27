import face_recognition
from PIL import Image, ImageDraw
import pickle
import os
import cv2
import numpy as np

# Const

cameras_for_monitoring = {'new6':[15]}
registrator_ip_port = {'new6':'192.168.11.53:554'}
rtsp_username = 'admin'
rtsp_password = ''
width = 1920
height = 1080

# Functions


def camera_capture(current_registrator_ip_port, channel):
    rtsp = f"rtsp://" + current_registrator_ip_port + \
          f"/user={rtsp_username}" + \
          f"&password={rtsp_password}" + \
          f"&channel={channel}"  + \
          f"&stream=0.sdp"
    print("rtsp=",rtsp)
    capture = cv2.VideoCapture()
    capture.open(rtsp)
    #print("capture=",dir(capture))
    return capture



def main():
    # Программа мониторинга лиц посетителей
    registrators = list(cameras_for_monitoring.keys())
    registrator_id = registrators[0]
    camera_number = cameras_for_monitoring[registrator_id][0]
    current_registrator_ip_port = registrator_ip_port[registrator_id]
    capture_obj = camera_capture(current_registrator_ip_port, str(camera_number))
    file_count = 0
    
    import os.path
    #path = os.path.realpath(cv2.__file__)
    #print("cv2=",path)
    #path = os.path.dirname(2.__file__)
    #print("cv2=",path)
    
    #while(capture_obj.isOpened()):
    while(file_count < 2):
        file_count += 1
        ret, current_frame = capture_obj.read()
        print(current_frame.shape)
        print(current_frame.dtype)
        print("ret, file_count=",ret,file_count)
        #print("current_frame=", type(current_frame))
        #print(dir(current_frame))
        if ret == True:
            writefile = f"/home/igladky/m_face_recognition/Data/Image_sequence/cam{camera_number}_{file_count}.jpg"
            image_directory = os.path.dirname(writefile)
            result = False;
            try:
                result = cv2.imwrite(writefile, current_frame)
            except cv2.error as e:
                # inspect error object
                print("e=",e)
                print(type(e))
                for k in dir(e):
                    if k[0:2] != "__":
                        print("e.%s = %s" % (k, getattr(e, k)))
                    # handle error: empty frame
                    if e.err == "!_src.empty()":
                        break # break the while loop
            #writeresult = cv2.imwrite(writefile, current_frame)
            print("writefile=",writefile)
            print("result=", result)
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




