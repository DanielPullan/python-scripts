## F1 Wallpaper Background Thing by Dan Pullan (https://danielpullan.co.uk)
## Grab a wallpaper from the F1Porn subreddit, convert it to black and white and set it as wallpaper.
## 03/08/2019

## import stuff here
import RedPy
from PIL import Image
import os

os.chdir("/wallpaper")

## download images from the subreddit
useragent = "Windows 10 : f1-wallpaper.py (By Dan Pullan) "
agent = RedPy.Redpy(useragent)

subreddit = sys.argv[0]
amount = sys.argv[1]

useragent.download(subreddit, number=amount, sort_option=None)

## convert to black and white
images = 0

for file in os.listdir("/wallpaper"):
		images = images + 1
		if file.endswith(".jpg")
			img = Image.open(file).convert('LA')
			finished_name = file + images + ".jpg"
			img.save(finished_name)

## move to wallpaper folder
## note: only files that start with done
