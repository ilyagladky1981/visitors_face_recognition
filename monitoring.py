import face_recognition
from PIL import Image, ImageDraw
import pickle
import os
import cv2

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
    path = os.path.realpath(cv2.__file__)
    print("cv2=",path)
    path = os.path.dirname(cv2.__file__)
    print("cv2=",path)
    
 bool result = false;
 try
 {
 result = imwrite("alpha.png", mat, compression_params);
 }
 catch (const cv::Exception& ex)
 {
 fprintf(stderr, "Exception converting image to PNG format: %s\n", ex.what());
 }
 if (result)
 printf("Saved PNG file with alpha data.\n");
 else
 printf("ERROR: Can't save PNG file.\n");

    #while(capture_obj.isOpened()):
    while(file_count < 2):
        file_count += 1
        ret, current_frame = capture_obj.read()
        print("ret, file_count=",ret,file_count)
        #print("current_frame=", type(current_frame))
        #print(dir(current_frame))
        if ret == True:
            writefile = f"/home/igladky/visitors_face_recognition/Resources/Image_sequence/cam{camera_number}_{file_count}.jpg"
            writeresult = cv2.imwrite(writefile, current_frame)
            print("writefile=",writefile)
            print("writeresult=", writeresult)
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




