import csv
import json

locations = {'AL': '',
            'AK': '',
            'AZ': '',
            'AR': '',
            'CA': '',
            'CO': '',
            'CT': '',
            'DE': '',
            'FL': '',
            'GA': '',
            'HI': '',
            'ID': '',
            'IL': '',
            'IN': '',
            'IA': '',
            'KS': '',
            'KY': '',
            'LA': '',
            'ME': '',
            'MD': '',
            'MA': '',
            'MI': '',
            'MN': '',
            'MS': '',
            'MO': '',
            'MT': '',
            'NE': '',
            'NV': '',
            'NH': '',
            'NJ': '',
            'NM': '',
            'NY': '',
            'NC': '',
            'ND': '',
            'OH': '',
            'OK': '',
            'OR': '',
            'PA': '',
            'RI': '',
            'SC': '',
            'SD': '',
            'TN': '',
            'TX': '',
            'UT': '',
            'VT': '',
            'VA': '',
            'WA': '',
            'WV': '',
            'WI': '',
            'WY': ''}

for key in locations:
  locations[key] = {'Anger': 0, 'Disgust':0, 'Fear': 0, 'Happiness': 0, 'Neutral': 0, 'Sadness': 0, 'Surprise': 0}

cr = csv.reader(open("finaldata.csv","rU"))
for row in cr:
  state = row[0]
  emotion = row[1]
  locations[state][emotion] += 1

for key in locations:
  sum = locations[key]['Anger'] + locations[key]['Disgust'] + locations[key]['Fear'] + locations[key]['Happiness'] + locations[key]['Neutral'] + locations[key]['Sadness'] + locations[key]['Surprise']
  for x in locations[key]:
    locations[key][x] = locations[key][x]/float(sum)

print json.dumps(locations, sort_keys=True, indent=2, separators=(',', ': '))

