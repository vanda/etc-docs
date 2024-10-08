import requests
import csv
import time 

object_ids = []
object_data = []
objects_csv = []

with open("object-list.csv", "r") as csv_file:
  csvreader = csv.reader(csv_file)
  for row in csvreader:
    object_ids.append(row[0])

# Retrieve APi data

for obj_id in object_ids:
  resp = requests.get(f"https://api.vam.ac.uk/v2/object/{obj_id}")
  obj_data = resp.json()
  print(obj_data['record']['objectType'])
  object_type = obj_data['record']['objectType']
  object_accession_num = obj_data['record']['accessionNumber']
  object_sys_num = obj_data['record']['systemNumber']
  if len(obj_data['record']['titles']) > 0:
    object_title = obj_data['record']['titles'][0]['title']
  if len(obj_data['meta']['images']) > 0:
    object_image = obj_data['meta']['images']['_iiif_image']
    object_image_id = obj_data['meta']['images']['_images_meta'][0]['assetRef']
  objects_csv.append([object_sys_num,object_type,object_title,object_image_id])

  # Retrieve images at fixed size
  if object_image:
    img_resp = requests.get(f"{object_image}/full/512,/0/default.jpg")
    with open(f"{object_sys_num}_{object_image_id}.jpeg", "wb") as img_file:
      img_file.write(img_resp.content)

with open(f"objects-data.csv", "w") as csv_file:
  csv_writer = csv.writer(csv_file)
  for obj in objects_csv:
    csv_writer.writerow(obj)

  exit(0)
