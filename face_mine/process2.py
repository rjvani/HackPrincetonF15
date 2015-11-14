import csv
import cv2
import numpy as np
import urllib
import os

B=2**12; # number of dimensions in our feature space

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
outfile = open("test2.csv", "w")
writer = csv.writer(outfile)

# write header and data
header = ["Url", "Category", "isAdultContent", "isRacyContent", "adultScore", "racyScore", "age", "gender", "dominantColorForeground", "dominantColorBackground", "accentColor", "emotion"]
for i in range(B):
  header.append("v"+str(i))
writer.writerow(header)

cr = csv.reader(open("test.csv","rU"))
imgNum = 0
for row in cr:
  # download image
  imageName = "data"+str(imgNum)+".jpg"
  print("processing image " + str(imgNum))
  urllib.urlretrieve(row[0], imageName)
  
  # convert color text to int value
  row[8] = colorToValue(row[8])
  row[9] = colorToValue(row[9])
  row = row[0:12]

  img = cv2.imread(imageName,0)

  # Initiate STAR detector
  orb = cv2.ORB_create()

  # find the keypoints with ORB
  kp = orb.detect(img,None)

  # compute the descriptors with ORB
  kp, des = orb.compute(img, kp)


  v=[0]*B; # initialize the vector to be all-zeros

  count = 0
  for i in range(len(kp)):
    desSum = 0
    for descVal in des[i]:
      desSum += descVal
    v[hash(kp[i].pt[0] * 7121 * desSum) % B]=1
    v[hash(kp[i].pt[1] * 6635609 * desSum) % B]=1
    count += 2
    
  for feature in v:
    row.append(feature)

  print count
  print sum(v)
    
  writer.writerow(row)
  imgNum += 1
  os.remove('/Users/marvin/HackPrinceton2015/HackPrincetonF15/face_mine/' + imageName)
  
outfile.close()

