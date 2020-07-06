import csv
import json

# get json file
with open('dataset.json') as json_file:
    data = json.load(json_file)

# open annotations csv
with open('annotations.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['image_name', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
    for i in range(len(data['images'])):
        # write to csv
        writer.writerow([data['images'][i]['file_name'], 
                            data['images'][i]['file_name'][:10], 
                            data['annotations'][i]['bbox'][0],
                            data['annotations'][i]['bbox'][1],
                            data['annotations'][i]['bbox'][0] + data['annotations'][i]['bbox'][2],
                            data['annotations'][i]['bbox'][1] + data['annotations'][i]['bbox'][3]])
