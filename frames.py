import sys
import os
from PIL import Image

images = []

for filename in os.listdir(sys.argv[1]):
    if filename.endswith('.gif'):
        images.append(Image.open(os.path.join(sys.argv[1], filename)))

images[0].save(
  "frames.gif",  save_all=True, append_images=images[1:], duration=200, loop=0
)