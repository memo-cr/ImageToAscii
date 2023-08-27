from PIL import Image
density = "Ñ@#W$90?!abc;:+=-,._ "
name = input("FILENAME: ")
with Image.open(name) as im:
    px = im.load()
with open("output.txt",'w') as file:
    pass
text=""
for i in range(im.height):
    for j in range(im.width):
        pixl= px[j,i]
        avg= (pixl[0]+pixl[1]+pixl[2])/3
        charInd= int(avg/(255/len(density)))
        text+=density[charInd-1] 
    text+="\n"
print(text)
# f = open("output.txt", "a")
# f.write(text)
# f.close()
print("Successfull")
