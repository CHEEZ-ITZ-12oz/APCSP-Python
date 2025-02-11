from PIL import Image
import random

# setup ................

img = Image.open("assets/Image/53.png") #    53    or     _gorgetest
width,height = img.size

# filters .................

def grayscale():
    for row in range(height):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            avg = int((rgb[0]+rgb[1]+rgb[2])/3)
            img.putpixel([pxl,row],tuple([avg,avg,avg]))
    img.save("assets/Image/colorgone.png")
    print("Image Grayed")

def mirrorTop2Bottom():
    for row in range(int(height/2)):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            img.putpixel([pxl,((height-1)-row)],rgb)
    img.save("assets/Image/f_mirrored.png")
    print("Image Mirrored")

def encodeImage():
    msg = Image.open("assets/Image/1message.png")
    for row in range(height):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            pxlgrab = msg.getpixel([pxl,row])
            #if pxlgrab == tuple([0,0,0]):
            if pxlgrab != tuple([255,255,255]):
                if rgb[0] % 2 == 0:
                    red = rgb[0] + 1
                    rgb = tuple([red,rgb[1],rgb[2]])
                img.putpixel([pxl,row],rgb)
            else:
                if rgb[0] % 2 != 0:
                    red = rgb[0] + 1
                    if red > 255: red = 254
                    rgb = tuple([red,rgb[1],rgb[2]])
                img.putpixel([pxl,row],rgb)
    img.save("assets/Image/k_encoded.png")
    print("Message Encoded")

def decodeImage():
    msg = Image.open("assets/Image/k_encoded.png")
    for row in range(height):
        for pxl in range(width):
            rgb = msg.getpixel([pxl,row])
            if rgb[0] % 2 == 0:
                msg.putpixel([pxl,row],tuple([255,255,255]))
            else:
                msg.putpixel([pxl,row],tuple([0,0,0]))
    msg.save("assets/Image/l_messageDecoded.png")
    print("Message Decoded")

def invert():
    for row in range(height):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            inv = tuple([255-rgb[0],255-rgb[1],255-rgb[2]])
            img.putpixel([pxl,row],inv)
    img.save("assets/Image/g_antimines.png")
    print("Image Inverted")
    
def pixilate():
    ps = 4 #pixel size (for 53, use 4 or 8)
    for row in range(0, height, ps):
        for blk in range(0, width, ps):
            rTotal = 0
            gTotal = 0
            bTotal = 0
            for irow in range(row,row+ps):
                for pixel in range(blk,blk+ps):
                    rgb = img.getpixel([pixel,irow])
                    rTotal += rgb[0]
                    gTotal += rgb[1]
                    bTotal += rgb[2]
            red = int(rTotal/(ps*ps))
            green = int(gTotal/(ps*ps))
            blue = int(bTotal/(ps*ps))
            for irow in range(row,row+ps):
                for pixel in range(blk,blk+ps):
                    img.putpixel([pixel,irow],tuple([red,green,blue]))
    img.save("assets/Image/g_psGraphics.png")
    print("Image Pixilated")
                    


def flipper():
    read = Image.open("assets/Image/53.png")
    for row in range(int(height)):
        for pxl in range(width):
            rgb = read.getpixel([pxl,row])
            img.putpixel([((width-1)-pxl),((height-1)-row)],rgb)
    img.save("assets/Image/h_E5.png")
    print("Image Flipped")

def shifty():
    for row in range(height):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            inv = tuple([rgb[1],rgb[2],rgb[0]])
            img.putpixel([pxl,row],inv)
    img.save("assets/Image/i_3shifted5.png")
    print("Image ColorShifted")

def combine():
    msg = Image.open("assets/Image/1message.png")
    for row in range(height):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            pxlgrab = msg.getpixel([pxl,row])
            r,g,b,alpha = rgb
            rg,gg,bg = pxlgrab
            r += int(rg/4)
            g += int(gg/4)
            b += int(bg/4)
            if r > 255: r == 255
            if g > 255: g == 255
            if b > 255: b == 255
            img.putpixel([pxl,row],tuple([r,g,b]))
    img.save("assets/Image/notSoSecret.png")
    print("Images Combined")

def blur():
    strength = 3
    read = Image.open("assets/Image/53.png")
    for row in range(int(height)):
        for pxl in range(width):
            x = pxl+random.randint(-strength,strength)
            y= row+random.randint(-strength,strength)
            if x < 0: x = 0
            if x >= width: x = width-1
            if y < 0: y = 0
            if y >= height: y = height-1
            rgb = read.getpixel([x,y])
            img.putpixel([pxl,row],rgb)
    img.save("assets/Image/j_fitft hyree.png")
    print("Image Scrambled")

def inverse():
    sav = Image.open("assets/Image/_blanksquare.png")
    for row in range(int(height)):
        for pxl in range(width):
            rgb = img.getpixel([pxl,row])
            sav.putpixel([row,pxl],rgb)
    sav.save("assets/Image/n^-1(53).png")
    print("Image Inversed")


# main .................
while True:
    try:
        print(f"Select a Filter.\n1 - Grayscale | 2 - Mirror | 3 - Invert | 4 - Pixilate | 5 - Rotate | 6 - Colorshift | 7 - Blur | 8 - Flip\n9 - Image Encoding | 10 - Image Decoding | 11 - Image Combination.")
        uinp = int(input("Enter Number: "))
        if uinp <= 9 and uinp >= 0:
            break
        else:
            print("Invalid selection. Try again.")
    except:
        print("Invalid input. Try again.")

if uinp == 1:
    grayscale()
elif uinp == 2:
    mirrorTop2Bottom()
elif uinp == 3:
    invert()
elif uinp == 4:
    pixilate()
elif uinp == 5:
    flipper()
elif uinp == 6:
    shifty()
elif uinp == 7:
    blur()
elif uinp ==8:
    inverse()
elif uinp == 9:
    encodeImage()
elif uinp == 10:
    decodeImage()
else:
    combine()
