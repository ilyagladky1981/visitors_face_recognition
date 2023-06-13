import face_recognition
from PIL import Image, ImageDraw
import pickle

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

def extract_faces(img_path)
  count = 0
  img_file = face_recognition.load_image_file(img_path)
  faces_location = face_recognition.face_locations(img_file)
  
  for face_location in faces_location:
    top, right, bottom, left = face_location
    
    face_img = img_file[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.save()
    count += 1
  
  return f"Found {count} face(s) in this photo"


def compare_faces(img1_path, img2_path):
  img1 = face_recognition.load_image_file(img1_path)
  img1_encodings = face_recognition.face_encodings(img1)[0]
  print(img1_encodings)
  
  img2 = face_recognition.load_image_file(img2_path)
  img2_encodings = face_recognition.face_encodings(img2)[0]
  
  result = face_recognition.compare_faces([img1_encodings], img2_encodings)
  print(result)
  
  if result[0]:
    print("Welcome to the club! :*")
  else:
    print("Sorry, not today... Next!")


def main():
  face_rec()



if __name__ == '__main__':
  main()
