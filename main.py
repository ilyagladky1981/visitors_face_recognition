import face_recognition


def face_rec():
<<<<<<< HEAD
  gal_face_img = face_recognition.load_image_file("img/gal1.gif")
=======
  gal_face_img = face_recognition.load_image_file("img/gal1.jpg")
>>>>>>> 3cb7603 (f)
  gal_face_location = face_recognition.face_locations(gal_face_img)
  
  justice_league_img = face_recognition.load_image_file("img/justice_league_actors.jpg")
  justice_league_faces_location = face_recognition.face_locations(justice_league_img)
  
  print(gal_face_location)
  print(justice_league_faces_location)
  print(f"Found {len(gal_face_location)} face(s) in this image")
  print(f"Found {len(justice_league_faces_location)} face(s) in this image")



def main():
  face_rec()



if __name__ == '__main__':
  main()
