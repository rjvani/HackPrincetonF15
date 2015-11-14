
from imgurpython import ImgurClient

PATH = "imgur.txt"
client_id = "YOUR CLIENT ID"
client_secret = "YOUR CLIENT SECRET"

client = ImgurClient(client_id, client_secret)

# CMU 15-112
def writeFile(filename, contents, mode="wt"):
  with open(filename, mode) as fout:
    fout.write(contents)

def main():
  result = ""
  items = client.gallery()
  extensionIndex = -4
  # get random images
  for item in items:
    # image link
    if item.link[extensionIndex] == ".":
      result += item.link + "\n"
  writeFile(PATH, result)

if __name__ == "__main__":
  main()

