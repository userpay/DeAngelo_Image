import Image, winsound
#from random import randint
im = Image.open("colorful_flower_frame-33px.jpg")
pix = im.load()
picsize = im.size #Get the width and hight of the image for iterating over
print picsize
width = picsize[0]
height = picsize[1]
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
        #print pix[x,y]
        if pixtotal != 255:
            #print pixtotal #Get the RGBA Value of the a pixel of an image
            if pixtotal < lowestpixel: #checks what lowest pixel thus far is
                lowestpixel = pixtotal
            if pixtotal > highestpixel: #checks what highest pixel thus far is except for 255
                highestpixel = pixtotal

rangepixel = highestpixel - lowestpixel

print "hightest pixel: ", highestpixel, " lowestpixel: ", lowestpixel, " rangepixel: ", rangepixel

pixeldivision = rangepixel/4.0

print "pixeldivision: ", pixeldivision

first = pixeldivision
second = first + first
third = second + first
fourth = third + first

print first, " ", second, " ", third, " ", fourth

for k in range(width):
    for r in range(height):
        x = k
        y = r
        g = 0
        pixel = 0
        #rndTime = randint(10,50)
        if type(pix[x,y]) == tuple:
            tuplength = len(pix[x,y])
            pixtup = pix[x,y]
            while g < tuplength:
                pixel = pixtup[g] + pixel
                g = g + 1
            pixtotal = pixel/tuplength
        else:
            pixtotal = pix[x,y]
        #print pix[x,y]
        print pixtotal #Get the RGBA Value of the a pixel of an image
        if pixtotal <= first:
            winsound.Beep(1000, rndTime)
        elif first < pixtotal <= second:
            winsound.Beep(2000, rndTime)
        elif second < pixtotal <= third:
            winsound.Beep(3000, rndTime)
        elif third < pixtotal <= fourth:
            winsound.Beep(4000, rndTime)
        elif fourth < pixtotal:
            winsound.Beep(5000, rndTime)

