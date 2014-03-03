import Image
im = Image.open("toei_sonic_16_bit_by_somesortofrobot-d327sgh.jpg")
pix = im.load()
picsize = im.size #Get the width and hight of the image for iterating over
print picsize
width = picsize[0]
height = picsize[1]
count = 0

for i in range(width):
    for j in range(height):
        x = i
        y = j
        if pix[x,y] != 255:
            print pix[x,y] #Get the RGBA Value of the a pixel of an image
        elif pix[x,y] == 255:
            count = count + 1

#counts how many pixels wern't outputted. Said pixels having a value of 255
print "count is ", count
