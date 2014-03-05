import Image, winsound
im = Image.open("toei_sonic_16_bit_by_somesortofrobot-d327sgh.jpg")
pix = im.load()
picsize = im.size #Get the width and hight of the image for iterating over
print picsize
width = picsize[0]
height = picsize[1]
count = 0
lowestpixel = 255
highestpixel = 0
rangepixel = 0
pixeldivision = 1


for i in range(width):
    for j in range(height):
        x = i
        y = j
        if pix[x,y] != 255:
            print pix[x,y] #Get the RGBA Value of the a pixel of an image
            if pix[x,y] < lowestpixel: #checks what lowest pixel thus far is
                lowestpixel = pix[x,y]
            if pix[x,y] > highestpixel: #checks what highest pixel thus far is except for 255
                highestpixel = pix[x,y]
        elif pix[x,y] == 255:
            count = count + 1

#counts how many pixels wern't outputted. Said pixels having a value of 255
print "count is ", count

rangepixel = highestpixel - lowestpixel

print "hightest pixel: ", highestpixel, " lowestpixel: ", lowestpixel, " rangepixel: ", rangepixel

pixeldivision = rangepixel/5.0

print "pixeldivision: ", pixeldivision

first = pixeldivision
second = first + first
third = second + first
fourth = third + first
fifth = fourth + first

print first, " ", second, " ", third, " ", fourth, " ", fifth

for i in range(width):
    for j in range(height):
        x = i
        y = j
        if pix[x,y] != 255:
            print pix[x,y] #Get the RGBA Value of the a pixel of an image
            if pix[x,y] <= first:
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            elif first < pix[x,y] <= second:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            elif second < pix[x,y] <= third:
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            elif third < pix[x,y] <= fourth:
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            elif fourth < pix[x,y] <= fifth:
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
