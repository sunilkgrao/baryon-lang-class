"""
Import sample data for classification engine
"""

import predictionio
import argparse

def import_events(client, file):
  f = open(file, 'r')
  count = 0
  print "Importing data..."
  for line in f:
    data = line.rstrip('\r\n').split(",")
    language = data[0]
    #Not strictly CSV, after the first comma, no longer delimiting
    text = ",".join(data[1:])

    if language == 'english':
        label = 1.0
    elif language == 'french':
        label = 2.0
    elif language == 'spanish':
        label = 3.0
    elif language == 'german':
        label = 4.0
    else:
        label = 0.0

    client.create_event(
      event="sentence",
      entity_type="content",
      entity_id=str(count), # use the count num as user ID
      properties= {
        "text" : text,
        "language" : language,
        "label" : label
      }
    )
    count += 1
  f.close()
  print "%s events are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for classification engine")
  parser.add_argument('--access_key', default='MizmlqlLX55Wgu9Y0aBYTxMUDA7jXyuuUmI9m94qEAvYk4C7fsjp7dRylzpKVGVH')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/languageData.txt")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
