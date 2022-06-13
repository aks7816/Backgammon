from cs1graphics import *

#########################################################################
w = float(input('Value of the number of pixels per grid-cell? '))
#########################################################################

paper = Canvas(6*w, 5.2*w, 'burlywood4', 'Backgammon')

midsection = Path(Point(3*w,0), Point(3*w,5.2*w))
midsection.setBorderWidth(3)
paper.add(midsection)

leftsec = Rectangle(2.4*w, 4.4*w, Point(1.6*w, 2.6*w))
leftsec.setFillColor('navajowhite')
leftsec.setBorderColor('navajowhite')
paper.add(leftsec)

rightsec = Rectangle(2.4*w, 4.4*w, Point(4.4*w,2.6*w))
rightsec.setFillColor('navajowhite')
rightsec.setBorderColor('navajowhite')
paper.add(rightsec)

###This is for the points for the left section###############################################

for a in range(int(.4*w), int(2.8*w), int(.40*w)):
    if a%(.16*w) != 0:
        redtribottom = Polygon(Point(a, 4.8*w), Point(a+.4*w, 4.8*w), Point(a+.20*w, 2.8*w))
        redtribottom.setFillColor('darkorange')
        paper.add(redtribottom)

for a in range(int(.4*w), int(2.8*w), int(.40*w)):
    if a%(.16*w) == 0:
        browntribottom = Polygon(Point(a, 4.8*w), Point(a+.40*w, 4.8*w), Point(a+.20*w, 2.8*w))
        browntribottom.setFillColor('tan')
        paper.add(browntribottom)


for a in range(int(.4*w), int(2.8*w), int(.40*w)):
    if a%(.16*w) == 0:
        redtritop = Polygon(Point(a, .40*w), Point(a+.40*w, .40*w), Point(a+.20*w, 2.4*w))
        redtritop.setFillColor('darkorange')
        paper.add(redtritop)

for a in range(int(.4*w), int(2.8*w), int(.40*w)):
    if a%(.16*w) != 0:
        browntritop = Polygon(Point(a, .40*w), Point(a+.40*w, .40*w), Point(a+.20*w, 2.40*w))
        browntritop.setFillColor('tan')
        paper.add(browntritop)

##This is for the points for right section#################################################

for a in range(int(3.20*w), int(5.60*w), int(.40*w)):
    if a%(.16*w) == 0:
        redtribottom2 = Polygon(Point(a, 4.80*w), Point(a+.40*w, 4.80*w), Point(a+.20*w, 2.80*w))
        redtribottom2.setFillColor('darkorange')
        paper.add(redtribottom2)

for a in range(int(3.20*w), int(5.60*w), int(.40*w)):
    if a%(.16*w) != 0:
        browntribottom2 = Polygon(Point(a, 4.80*w), Point(a+.40*w, 4.80*w), Point(a+.20*w, 2.80*w))
        browntribottom2.setFillColor('tan')
        paper.add(browntribottom2)

for a in range(int(3.20*w), int(5.60*w), int(.40*w)):
    if a%(.16*w) != 0:
        redtritop2 = Polygon(Point(a, .40*w), Point(a+.40*w, .40*w), Point(a+.20*w, 2.40*w))
        redtritop2.setFillColor('darkorange')
        paper.add(redtritop2)

for a in range(int(3.20*w), int(5.60*w), int(.40*w)):
    if a%(.16*w) == 0:
        browntritop2 = Polygon(Point(a, .40*w), Point(a+.40*w, .40*w), Point(a+.20*w,2.40*w))
        browntritop2.setFillColor('tan')
        paper.add(browntritop2)


###For numbers on the left bottom############################

count = .20*w
for n in range(1,7):
    num = Text(str(n))
    num.setFontSize(.15*w)
    count = count + .40*w 
    num.move(count, 5.00*w)
    paper.add(num)

###For the numbers on the right bottom#################################

count = .20*w
for n in range(7,13):
    num2 = Text(str(n))
    num2.setFontSize(.15*w)
    count = count + .40*w 
    num2.move(count+2.80*w, 5.00*w)
    paper.add(num2)

###For the numbers on the left top######################################

count = .20*w
for n in range(24,18,-1):
    num3 = Text(str(n))
    num3.setFontSize(.15*w)
    count = count + .40*w 
    num3.move(count, .20*w)
    paper.add(num3)

###For the numbers on the right top######################################

count = .20*w
for n in range(18,12,-1):
    num4 = Text(str(n))
    num4.setFontSize(.15*w)
    count = count + .40*w 
    num4.move(count+2.80*w, .20*w)
    paper.add(num4)


###Coins##################################################


###Coins on top################################################################################    
    
count = .40*w
x = 1
for Num,pt,whiteOnTop in [(2,.60*w,True), (5,2.60*w,False), (3,3.80*w,False), (5,5.40*w,True)]:
    if whiteOnTop is True:
        count = .40*w
        for x in range(Num):
            Coin = Circle(.18*w, Point(pt,.20*w+ count))
            count = count +.36*w
            Coin.setFillColor('white')
            paper.add(Coin)
            x += 1
    else:
        count = .40*w
        for x in range(Num):
            Coin = Circle(.18*w, Point(pt,.20*w+ count))
            count = count +.36*w
            Coin.setFillColor('black')
            paper.add(Coin)
            x += 1
        
###Coins on the bottom#############################################################################
                  
count = .40*w
x = 1
for Num,pt,whiteOnBottom in [(2,.60*w,True), (5,2.60*w,False), (3,3.80*w,False), (5,5.40*w,True)]:
    if whiteOnBottom is True:
        count = .40*w
        for x in range(Num):
            Coin = Circle(.18*w, Point(pt,5.00*w-count))
            count = count +.36*w
            Coin.setFillColor('black')
            paper.add(Coin)
            x += 1
    else:
        count = .40*w
        for x in range(Num):
            Coin = Circle(.18*w, Point(pt,5.00*w-count))
            count = count +.36*w
            Coin.setFillColor('white')
            paper.add(Coin)
            x += 1
        




    












    
    







