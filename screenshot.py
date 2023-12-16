import pyscreenshot as p
def ss():
    image = p.grab()
    image.show()
    image.save("screen.jpg")
def ssp(x1,x2,y1,y2):
    image = p.grab(bbox=(x1,x2,y1,y2))
    image.show()
    image.save("screen.jpg")
choice = int(input("Press 1 to capture wholescreen \n or Press 2 to capture partial screenshot"))
if choice==1:
    ss()
else:
    x1,x2,y1,y2= map(int,input("Enter the pixel positions in the order x1 x2 y1 y2").split())
    ssp(x1,x2,y1,y2)

