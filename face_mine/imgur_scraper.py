
from imgurpython import ImgurClient

PATH = "imgur1.txt"
client_id = 'b68fbc6850008f8'
client_secret = 'b83cc295315d15e167a61d3a8a572ee5bf42d731'

imgur_client = ImgurClient(client_id, client_secret)
imgur_gallery = imgur_client.gallery()

# CMU 15-112
def writeFile(filename, contents, mode="wt"):
  with open(filename, mode) as fout:
    fout.write(contents)

def main():
  result = ""
  items = imgur_gallery
  extensionIndex = -4
  # get random images
  for item in items:
    # image link
    if item.link[extensionIndex] == ".":
      result += item.link + "\n"
  writeFile(PATH, result)

if __name__ == "__main__":
  main()

