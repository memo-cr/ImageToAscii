from PIL import Image
density = "Ñ@#W$9876543210?!abc;:+=-,._ "
with Image.open("baris3.png") as im:
    px = im.load()
text=""
for j in range(im.size[0]):
    for i in range(im.size[1]):
        pixl= px[j,i]
        avg= (pixl[0]+pixl[1]+pixl[2])/3
        charInd= int(avg/(255/len(density)))
        text+=density[charInd-1] 
    text+="\n"
print(text)
