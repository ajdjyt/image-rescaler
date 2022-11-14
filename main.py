from PIL import Image
import math,os
inp="main.jpeg"
try:
    os.chdir(input("Enter directory of image: "))
    inp=input("Enter the name of the image: ")
    im=Image.open(inp)
except:
    print("Error opening image.")
presets={"4k":[3840,2160],"2k":[2048,1080],"1080p":[1920,1080],"720p":[1280,720],"480p":[720,480],"360p":[480,360],"240p":[426,240]}
presetq=input("Use a preset? ")
if presetq.lower() in ["y","yes"]:
    print("Choose one of the following presets:")
    presetlist=""
    for i in presets.keys():
        presetlist+=i+" "
    print(presetlist)
    preset=input(": ")
    if preset in presets:
        h,v=presets[preset]
    else:
        print("Invalid preset")
        exit()
else:
    try:
        m=float(input("Scale to? "))
    except:
        print("Enter valid values")
        exit()
    h=math.floor(m*im.width)
    v=math.floor(m*im.height)
out=im.resize((h,v),resample=1,reducing_gap=3) # Use the LANCZOS Filter with a reducing gap of 3
out.show()
try:
    os.chdir(input("Enter directory to save in: "))
    im.save(input("Name to save as: "))
except:
    print("Invalid folder path/file name")