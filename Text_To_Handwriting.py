#Importing Library
from PIL import Image

#Open the text file which you have to convert into handwriting

txt=open("dummy.txt")   # path of your text file
BG=Image.open("myfont/bg.png") #path of page(background)photo (I have used blank page)
sheet_width=BG.width
gap, ht = 0, 0


for i in txt.read().replace("\n",""):
        try:
                cases = Image.open("myfont/{}.jpg".format(str(ord(i))))
                offset = 0
                if(i.lower() in "gjpy,.'--z"):
                        offset = 12
                BG.paste(cases, (gap, ht + offset))
                size = cases.width
                height=cases.height
                #print(size)
                gap+=size

                if sheet_width < gap or len(i)*115 >(sheet_width-gap):
                    gap,ht=0,ht+75
        except:
                continue
print(gap)
print(sheet_width)
BG.save("text.png")

