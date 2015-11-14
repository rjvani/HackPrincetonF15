
import numpy as np
import cv2

def run():

  FILEPATH = "./test.png"
  port = 0
  frames = 30
  camera = cv2.VideoCapture(port)

  def getImage():
    (result, im) = camera.read()
    return im

  def get(camera):
    # go through frame rate to capture image
    for index in range(frames):
      pic = getImage()
    cv2.imwrite(FILEPATH, pic)
    del(camera)

  get(camera)

if __name__ == "__main__":
  run()
