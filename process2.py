import csv

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
  return 0

# open output file and get a csv writer
outfile = open("test2.csv", "a")
writer = csv.writer(outfile)

# write header and data
header = ["Url", "Category", "isAdultContent", "isRacyContent", "adultScore", "racyScore", "age", "gender", "dominantColorForeground", "dominantColorBackground", "accentColor", "emotion"]
writer.writerow(header)

cr = csv.reader(open("test.csv","rU"))
for row in cr:    
  row[8] = colorToValue(row[8])
  row[9] = colorToValue(row[9])
  row = row[0:12]
  writer.writerow(row)

outfile.close()

