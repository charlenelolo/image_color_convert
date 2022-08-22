from PIL import Image
import os

for file in os.listdir('orig'):  #for all the documents in the file
	if file.endswith('.jpg'):
		image_file = Image.open('orig/' + file)
		image_file = image_file.convert('L')
		image_file.save('result/' + file[:-4] + '_grey.png')

