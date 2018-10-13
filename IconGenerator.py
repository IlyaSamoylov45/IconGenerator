import hashlib
import os
import errno
from PIL import Image, ImageDraw

def main():
        #get user input and hash it
        name = input("Make an Icon!, Choose your username!\n")
        m = hashlib.sha384()
        name = name.encode('utf-8')
        m.update(name)

        #Get the Hexadecimal value of the md5 hash
        hexed = m.hexdigest()

        #split the hexadecimal values by two and then convert them to decimals
        hexed_array = [int(hexed[i:i+2],16) for i in range(0, len(hexed), 2)]

        #Set color of the Icon
        red = hexed_array[45]
        green = hexed_array[46]
        blue =  hexed_array[47]

        #set width and height of image
        width = 450
        height = 450

        #Create new image
        img = Image.new('RGB', (width, height), color = (255, 255, 255))
        x0 = 0
        x1 = 50
        y0 = 0
        y1 = 50
        index = 0;
        i = 0;
        #check each row
        while i < 9:
            j = 0
            mirror = [0 , 0 , 0, 0]
            #left of icon is filled in
            while j < 5:
                if hexed_array[index]%2 == 0:
                    d = ImageDraw.Draw(img)
                    d.rectangle([x0, y0, x1, y1], fill=(red,green,blue))
                    #The array will check which blocks on the left side will be mirrored on the right
                    if j == 0:
                        mirror[3] = 1
                    if j == 1:
                        mirror[2] = 1
                    if j == 2:
                        mirror[1] = 1
                    if j == 3:
                        mirror[0] = 1
                index += 1
                x0 += 50
                x1 += 50
                j += 1
            #fill in the right of icon based on mirror array
            for x in mirror:
                if(x == 1):
                    d = ImageDraw.Draw(img)
                    d.rectangle([x0, y0, x1, y1], fill=(red,green,blue))
                x0 += 50
                x1 += 50
            x0 = 0
            x1 = 50
            y0 += 50
            y1 += 50
            i += 1

        #Make a directory if it does not exist
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'Icons')
        try:
            os.makedirs(final_directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        #Make png based on input given by user in beginning of program
        name = name.decode() + '.png'
        if(len(name) > 30):
            name = name[0:30] + '.png'
        if(name == '.png'):
            name = 'THIS_IS_AN_EMPTY_STRING_SO_I_MADE_THIS_A_SPECIFIC_SAVED_IMAGE.png'
        #Makes the path the folder and saves the image to folder
        fullpath = os.path.join(final_directory, name)
        img.save(fullpath)
if __name__== "__main__":
  main()
