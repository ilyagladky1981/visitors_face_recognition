import face_recognition
from PIL import Image, ImageDraw
import pickle
import os
import cv2

def face_rec():
  gal_face_img = face_recognition.load_image_file("img/gal1.jpg")
  gal_face_location = face_recognition.face_locations(gal_face_img)
  
  justice_league_img = face_recognition.load_image_file("img/justice_league_actors.jpg")
  justice_league_faces_location = face_recognition.face_locations(justice_league_img)
  
  print(gal_face_location)
  print(justice_league_faces_location)
  print(f"Found {len(gal_face_location)} face(s) in this image")
  print(f"Found {len(justice_league_faces_location)} face(s) in this image")
  
  pil_gal_face_img = Image.fromarray(gal_face_img)
  draw_gal_face_img = ImageDraw.Draw(pil_gal_face_img)
  
  for(top, right, bottom, left) in gal_face_location:
    draw_gal_face_img.rectangle(((left, top), (right, bottom)), outline=(255, 87, 51), width=10)
  
  pil_gal_face_img.save("img/new_gal1.jpg")
  del draw_gal_face_img
  
  pil_justice_league_img = Image.fromarray(justice_league_img)
  draw_justice_league_img = ImageDraw.Draw(pil_justice_league_img)
  
  for(top, right, bottom, left) in justice_league_faces_location:
    draw_justice_league_img.rectangle(((left, top), (right, bottom)), outline=(255, 87, 51), width=10)
  
  pil_justice_league_img.save("img/new_justice_league.jpg")
  del draw_justice_league_img

def extract_faces(img_path):
  count = 0
  input_file_basename = os.path.basename(img_path)
  input_file_name = os.path.splitext(input_file_basename)[0]
  img_file = face_recognition.load_image_file(img_path)
  faces_location = face_recognition.face_locations(img_file)
  
  for face_location in faces_location:
    top, right, bottom, left = face_location
    
    face_img = img_file[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.save(f"img/{input_file_name}_{count}_face_img.jpg")
    count += 1
  
  return f"Found {count} face(s) in this photo"


def compare_faces(img1_path, img2_path):
  img1 = face_recognition.load_image_file(img1_path)
  img1_encodings = face_recognition.face_encodings(img1)[0]
  # print(img1_encodings)
  
  img2 = face_recognition.load_image_file(img2_path)
  img2_encodings = face_recognition.face_encodings(img2)[0]
  
  result = face_recognition.compare_faces([img1_encodings], img2_encodings)
  print(result)
  
  if result[0]:
    print("Welcome to the club! :*")
  else:
    print("Sorry, not today... Next!")


def detect_person_in_video():
  data = pickle.loads(open("Person_name_encodings.pickle", "rb").read())
  video = cv2.VideoCapture("video.mp4")
  
  while True:
    ret, image = video.read()
    
    locations = face_recognition.face_locations(image, model="cnn")
    encodings = face_recognition.face_encodings(image, locations)
    
    for face_encoding, face_location in zip(encodings, locations):
      result = face_recognition.compare_faces(data["encodings"], face_encoding)
      match = None
      
      if True in result:
        match = data["name"]
        print(f"Match found! {match}")
      else:
        print("ACHTUNG! ALARM!")
        
        left_top = (face_location[3], face_location[0])
        right_bottom = (face_location[1], face_location[2])
        color = [0, 255, 0]
        cv2.rectangle(image, left_top, right_bottom, color, 4)
        
        left_bottom = (face_location[3], face_location[2])
        right_bottom = (face_location[1], face_location[2] + 20)
        cv2.rectangle(image, left_bottom, right_bottom, color, cv2.FILLED)
        cv2.putText(
                image,
                match,
                (face_location[3] + 10, face_location[2] + 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                4
            )
      
      cv2.imshow("detect_person_in_video is running", image)
      
      k = cv2.waitKey(20)
      if k == ord("q"):
        print("Q pressed, closing the app")
        break


def main():
  # face_rec()
  # print(extract_faces("img/justice_league_actors.jpg"))
  compare_faces("img/gal1.jpg", "img/gal2.jpg")


if __name__ == '__main__':
  main()
