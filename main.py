from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import csv 
import time 


#initialize timer
start = time.time()

#read data from name.csv to get name list 
rows = []
with open('name.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)

#open certificate template
try:
    img = Image.open('award.png')
except IOError:
    pass

#get certificate width and height
w,h=img.size

#initialize counter
counter = 0

#ask user for output folder name 
output_folder = input('Output folder name: ')

#loop through each name in name list 
for i in range(len(rows)):
    open certificate template
    try:
        img = Image.open('award.png')
    except IOError:
        pass
    #get name, country, contribution from name list
    name = rows[i][0]
    committee = rows[i][1]
    country = rows[i][2]
    contribution = f'{committee} ({country})'

    #set fonts and font size to insert text in image
    f1 = ImageFont.truetype('Coco-Gothic-Regular-trial.ttf', 65)
    f2 = ImageFont.truetype('Coco-Gothic-Regular-trial.ttf', 45)
    I1 = ImageDraw.Draw(img)

    #add text to image
    I1.text(((122/297)*w, (115/210)*h), name, font=f1, fill=(0, 0, 0) )
    I1.text(((165/297)*w, (145/210)*h), contribution, font=f2, fill=(0, 0, 0) )

    #save image 
    img.save(f'./{output_folder}/img{name}.png')

    counter += 1

#stop timer
end = time.time()

#print execution data 
print(f'Time: {end-start}')
print(f'Certificates Printed: {counter}')

