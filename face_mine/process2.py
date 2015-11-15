import csv
import cv2
import numpy as np
import urllib
import os

B=2**12 # number of dimensions in our feature space

def colorToValue(color):
  if color == "Black":
    return int("000000", 16)
  if color == "Blue":
    return int("0000ff", 16)
  if color == "Brown":
    return int("a52a2a", 16)
  if color == "Grey":
    return int("8c8c8c", 16)
  if color == "Green":
    return int("008000", 16)
  if color == "Orange":
    return int("ffa500", 16)
  if color == "Pink":
    return int("ffc0cb", 16)
  if color == "Purple":
    return int("800080", 16)
  if color == "Red":
    return int("ff0000", 16)
  if color == "White":
    return int("ffffff", 16)
  if color == "Yellow":
    return int("ffff00", 16)
  if color == "Teal":
    return int("008080", 16)
  return color

# open output file and get a csv writer
outfile = open("test3.csv", "w")
writer = csv.writer(outfile)

# write header and data
header = ["Url", "emotion"]
for i in range(B):
  header.append("v"+str(i))
writer.writerow(header)

cr = csv.reader(open("testc.csv","rU"))
imgNum = 0
for row in cr:
  # download image
  imageName = "data"+str(imgNum)+".jpg"
  print("processing image " + str(imgNum))
  urllib.urlretrieve(row[0], imageName)
  
  # convert color text to int value
  c1 = colorToValue(row[8])
  c2 = colorToValue(row[9])
  c3 = row[10]
  aScore = row[4]
  rScore = row[5]
  age = row[6]
  gender = row[7]
  row = row[:1] + row[11:12]

  img = cv2.imread(imageName,0)

  # Initiate STAR detector
  orb = cv2.ORB_create()

  # find the keypoints with ORB
  kp = orb.detect(img,None)

  # compute the descriptors with ORB
  kp, des = orb.compute(img, kp)

  v=[0]*B; # initialize the vector to be all-zeros

  fraction = B/9
  v[hash(c1) % fraction]=1
  v[(hash(c2) % fraction) + fraction]=1
  v[(hash(c3) % fraction) + 2*fraction]=1
  v[(hash(aScore * 24953) % fraction) + 3*fraction]=1
  v[(hash(rScore * 30707) % fraction) + 4*fraction]=1
  v[(hash(age * 34129) % fraction)+ 5*fraction]=1
  v[(hash(gender * 41227) % fraction) + 6*fraction]=1

  for i in range(len(kp)/10):
    desSum = 0
    # for descVal in des[i]:
    #   desSum += descVal
    v[(hash(kp[i].pt[0] * 7121) % fraction) + 7*fraction]=1
    v[(hash(kp[i].pt[1] * 6635609) % fraction) + 8*fraction]=1
    
  for feature in v:
    row.append(feature)
    
  writer.writerow(row)
  imgNum += 1
  os.remove('/Users/marvin/HackPrinceton2015/HackPrincetonF15/face_mine/' + imageName)
  
outfile.close()

