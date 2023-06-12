import face_recognition
from PIL import Image, ImageDraw

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
     draw_gal_face_img.rectangle(((left, top), (right, bottom)), outline=(255, 87, 51), width=4)
  pil_gal_face_img.save("img/new_gal1.jpg")
  del draw_gal_face_img

def main():
  face_rec()



if __name__ == '__main__':
  main()
