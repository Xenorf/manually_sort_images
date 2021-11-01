import cv2
import os


def initializeFolders():
    try:
            os.mkdir(src_directory)
    except:
        print(src_directory+" folder already exist")
    for k in key_set :
        try:
            os.mkdir(src_directory+"/"+key_set[k])
        except:
            print(key_set[k]+" folder already exist")

def imageProcessing(preview_size = 900):
    for filename in os.listdir(src_directory+"/src"):
        if not filename.endswith(".jpeg"):
            continue
        print(filename)
        image = cv2.imread(src_directory+"/src/"+filename)
        height, width, channels = image.shape
        if height > width :
            ratio = preview_size/height
            width = int(ratio*width)
            height=preview_size
        else :
            ratio = preview_size/width
            height = int(ratio*height)
            width=preview_size
        resized_image = cv2.resize(image,(width,height))

        cv2.imshow('image', resized_image)
        key=0
        while chr(key) not in key_set :
            key = cv2.waitKey(0) & 0xFF
            print(chr(key))
        print("moved in "+key_set[chr(key)])
        os.replace(src_directory+"/src/"+filename, src_directory+"/"+key_set[chr(key)]+"/"+filename)

key_set = {
    't':"trash",
    'm':"me",
    'l':"landscape",
    'o':"other",
    's':"src"
    }
src_directory = 'images'

initializeFolders()
imageProcessing(preview_size = 900)