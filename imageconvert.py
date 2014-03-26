import Image, winsound, random  #WARNING Windows OS only

im = Image.open("50236_173144168270_6834_q.jpg") #opens image
pix = im.load() #loads image in
picsize = im.size #Get the width and hight of the image for iterating over
print picsize #outputs picture size, mostly for debug purposes
width = picsize[0] 
height = picsize[1]
lowestpixel = 255 #setting pixel values such that they'll 
highestpixel = 0 #    increment or decrement properly
rangepixel = 0
pixeldivision = 1
pixel = 1
#pixtup = 0
pixtotal = 0
tuplength = 0
random.seed()

for i in range(width):   #this loop is for establishing several variables
    for j in range(height): #   which are then used later on
        x = i
        y = j
        g = 0
        pixel = 0
        if type(pix[x,y]) == tuple:  #checks if pixels are a tuple/array
            pixtotal = 0
            tuplength = len(pix[x,y]) #gets length of pixel array
            pixtup = pix[x,y] #saves pixel tuple to a variable
            while g < tuplength: #converts tuple to a single variable
                pixel = pixtup[g] + pixel
                g = g + 1
            pixtotal = pixel/tuplength #reduces large variable to something closer to actual pixel values
        else: #if pixels are only 1 value and not a tuple/array
            pixtotal = pix[x,y]
        #print pix[x,y]
        if pixtotal != 255:
            #print pixtotal #Get the RGBA Value of the a pixel of an image
            if pixtotal < lowestpixel: #checks what lowest pixel thus far is
                lowestpixel = pixtotal
            if pixtotal > highestpixel: #checks what highest pixel thus far is except for 255
                highestpixel = pixtotal

rangepixel = highestpixel - lowestpixel #finds the pixel range

print "hightest pixel: ", highestpixel, " lowestpixel: ", lowestpixel, " rangepixel: ", rangepixel

pixeldivision = rangepixel/4.0 #This and following few lines establish divisions
#                                 which will be used for generating sounds
print "pixeldivision: ", pixeldivision

first = pixeldivision
second = first + first
third = second + first
fourth = third + first

print first, " ", second, " ", third, " ", fourth

for k in range(width):   #This is what actually plays the sounds
    for r in range(height):
        x = k
        y = r
        g = 0
        pixel = 0
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
        #print pixtotal #Get the RGBA Value of the a pixel of an image

        #These use beep fuction from Windows to produce specific tones with randomized length
        if pixtotal <= first:
            winsound.Beep(1000, random.randint(100, 400))
        elif first < pixtotal <= second:
            winsound.Beep(2000, random.randint(100, 400))
        elif second < pixtotal <= third:
            winsound.Beep(3000, random.randint(100, 400))
        elif third < pixtotal <= fourth:
            winsound.Beep(4000, random.randint(100, 400))
        elif fourth < pixtotal:
            winsound.Beep(5000, random.randint(100, 400))
        else:
            winsound.Beep(6000, random.randint(100, 400))
