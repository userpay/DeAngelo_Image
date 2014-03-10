import Image, winsound
im = Image.open("colorful_flower_frame-33px.jpg")
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
pixel = 1
#pixtup = 0
pixtotal = 0
tuplength = 0

for i in range(width):
    for j in range(height):
        x = i
        y = j
        g = 0
        pixel = 0
        if type(pix[x,y]) == tuple:
            pixtotal = 0
            tuplength = len(pix[x,y])
            pixtup = pix[x,y]
            while g < tuplength:
                pixel = pixtup[g] + pixel
                g = g + 1
            pixtotal = pixel/tuplength
        else:
            pixtotal = pix[x,y]
        print pixtotal
        if pixtotal != 255:
            print pixtotal #Get the RGBA Value of the a pixel of an image
            if pixtotal < lowestpixel: #checks what lowest pixel thus far is
                lowestpixel = pixtotal
            if pixtotal > highestpixel: #checks what highest pixel thus far is except for 255
                highestpixel = pixtotal
        elif pixtotal == 255:
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
        if pixtotal != 255:
            print pixtotal #Get the RGBA Value of the a pixel of an image
            if pixtotal <= first:
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            elif first < pixtotal <= second:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            elif second < pixtotal <= third:
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            elif third < pixtotal <= fourth:
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            elif fourth < pixtotal <= fifth:
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

