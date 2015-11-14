import sys
import numpy as np

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import requests
import os
import time
from PIL import Image
from StringIO import StringIO

def loadDataSet():

  port = 0
  frames = 30
  camera = cv2.VideoCapture(port)

  def getImage():
    (result, im) = camera.read()
    return im

  # CMU 15-112
  def writeFile(filename, contents, mode="wt"):
    with open(filename, mode) as fout:
      fout.write(contents)

  # CMU 15-112
  def readFile(filename, mode="rb"):
    with open(filename, mode) as fin:
      return fin.read()

  def loadImages(filePath):
    fileList = [ ]
    contents = readFile(filePath)
    for line in contents.splitlines():
      fileList += [line]
    return fileList

  def loadCounter(filePath):
    contents = None
    try:
      contents = int(readFile(filePath).splitlines()[0])
    except:
      contents = 0
    contents += 1
    writeFile(filePath, str(contents))
    return contents

  def get(camera, filePath):
    # go through frame rate to capture image
    for index in range(frames):
      pic = getImage()
    cv2.imwrite(filePath, pic)
    del(camera)

  def run():
    path = "imgur.txt"
    counterPath = "counter.txt"
    fileList = loadImages(path)
    counter = loadCounter(counterPath)
    finalPath = "faces" + os.sep + str(counter) + ".png"
    url = fileList[counter]
    response = requests.get(url)
    img = Image.open(StringIO(response.content))
    img.show()
    time.sleep(1)
    get(camera, finalPath)

  run()

if __name__ == "__main__":
  loadDataSet()
