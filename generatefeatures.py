import pyoxford
import csv

api = pyoxford.vision("ee629b252bb9449ab6da07d05dfe00e8")

# open output file and get a csv writer
outfile = open("test.csv", "w")
writer = csv.writer(outfile)

# write header and data
header = ["Url", "Category", "isAdultContent", "isRacyContent", "adultScore", "racyScore", "age", "gender", "dominantColorForeground", "dominantColorBackground", "accentColor", "emotion"]
# writer.writerow(header)

f = open('imgurl.csv')
imgUrlSet = csv.reader(f)

for url in imgUrlSet:
  imgUrl = url[0]
  result = api.analyze(imgUrl)

  category = result.categories[0].name

  isAdultContent = 0
  isRacyContent = 0
  adultScore = 0
  racyScore = 0

  if result.adult != None:
    isAdultContent = 1 if result.adult.isAdultContent else 0
    isRacyContent = 1 if result.adult.isRacyContent else 0  
    adultScore = result.adult.adultScore
    racyScore = result.adult.racyScore

  age = 0
  gender = 0
  count = 0
  
  for face in result.faces:
    age += face.age
    gender += 1 if face.gender == 'Male' else 0
    count += 1

  count = (1 if count == 0 else count)
  age = age / float(count)
  gender = gender / float(count)

  colorForeground = ""
  colorBackground = ""
  accentColor = ""

  if result.color != None:
    colorForeground = result.color.dominantColorForeground
    colorBackground = result.color.dominantColorBackground
    accentColor = int(result.color.accentColor, 16)

  r = [imgUrl, category, isAdultContent, isRacyContent, adultScore, racyScore, age, gender, colorForeground, colorBackground, accentColor, "none"]
  writer.writerow(r)

outfile.close()