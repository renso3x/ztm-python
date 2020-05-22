#Excercise: Convert an image from jpg to png

import sys
import os
from PIL import Image

read_from = sys.argv[1]
write_to = sys.argv[2]

if not os.path.exists(write_to):
  os.mkdir(write_to)

else:
  entries = os.listdir(read_from)

  for img in entries:
    new_img = Image.open(f'{read_from}{img}')
    clean_name = os.path.splitext(img)[0]
    # save to new/ directory file
    new_img.save(f'{write_to}{clean_name}.png', 'png')
