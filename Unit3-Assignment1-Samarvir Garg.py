import pygame
import math
import random

pygame.init()
SIZE=(1000,700)
screen = pygame.display.set_mode(SIZE)

# All colours that are being used    
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
ORANGE=(255,69,0)
BROWN=(150,75,0)
WHITE=(255,255,255)
RIVER_BLUE=(31, 81, 255)
WALL=(230, 161, 2)
RED=(255,0,0)
BLACK=(0,0,0)
GREY=(211,211,211)
WINDOW_BLUE=(164,219,232)
DARK_GREEN=(1,50,32)
YELLOW=(255, 255, 0)

# Function to draw a line
def line(color,x1,y1,x2,y2):
    pygame.draw.line(screen,color,(x1,y1),(x2,y2))
    pygame.display.flip()

# Function to draw a rectangle    
def rectangle(color,x,y,w,h):
    pygame.draw.rect(screen,color, (x, y, w, h))
    pygame.display.flip()

# Function to draw a ellipse    
def ellipse(COLOR,x, y, w, h):
    pygame.draw.ellipse(screen,COLOR, (x, y, w, h) )
    pygame.display.flip()
 
# Function to draw a arc   
def arc(COLOR,x,y,w,h,startAngle, endAngle):
    pygame.draw.arc(screen,COLOR,(x,y,w,h),startAngle, endAngle)
    pygame.display.flip()
 
# Function to draw a circle   
def circle(COLOR,x, y,radius):
    pygame.draw.circle(screen,COLOR,(x, y),radius)
    pygame.display.flip()

# Function to draw a cloud    
def cloud(x,y):
    ellipse(WHITE,x, y,100,40)
    ellipse(WHITE,x+20, y-10,100,30)
    ellipse(WHITE,x+20, y+10,100,30)
    ellipse(WHITE,x+40, y,100,40)
    pygame.display.flip()
    
#  Function to draw a tree    
def tree(x,y):
    circle(DARK_GREEN,x-20, y-20,60)
    circle(DARK_GREEN,x+70, y-20,60)
    circle(DARK_GREEN,x+25, y-70,60)
    rectangle(BROWN,x,y,50,150)
    pygame.display.flip()
 
# Function to draw a bird   
def bird(x,y):
    arc(BLACK,x,y,40,20,0,math.pi/2)
    arc(BLACK,x+40,y,40,20,math.pi/2,math.pi)
    pygame.display.flip()

# Function to draw a flower    
def flower(x,y):
    rectangle(DARK_GREEN,x,y,5,20)
    circle(WHITE,x-2.5,y,6)
    circle(WHITE,x+7.5,y,6)
    circle(WHITE,x-2.5,y-7.5,6)
    circle(WHITE,x+7.5,y-7.5,6)
    circle(YELLOW,x+2.5,y-4,5)
    pygame.display.flip()
    

rectangle(BLUE,0,0,1000,250) # to draw sky
circle(ORANGE,500,250,200) # to draw sun
rectangle(GREEN,0,250,1000,550) # to display the green field

# To draw smile face of sun
circle(BLACK,470,80,10) 
circle(BLACK,530,80,10)
arc(BLACK,450,100,100,60,math.pi,2*math.pi)

# To display the mountains
pygame.draw.polygon(screen,BROWN,((0,250),(250,20),(500,250)))
pygame.draw.polygon(screen,BROWN,((500,250),(750,20),(1000,250)))

# To display the river
pygame.draw.polygon(screen,RIVER_BLUE,((400,250),(550,250),(200,700),(0,700)))

# To display ice on top of mountain
pygame.draw.polygon(screen,WHITE,((250,20),(225,43),(275,43)))
pygame.draw.polygon(screen,WHITE,((750,20),(725,43),(775,43)))

# To display the walls of the house and roof
pygame.draw.polygon(screen, WALL, ((550, 400), (900, 400), (900, 600), (550, 600)))
pygame.draw.polygon(screen, RED, ((550, 400), (700, 400), (625, 300)))
pygame.draw.polygon(screen, RED, ((700, 400), (900, 400), (825, 300), (625, 300)))

# To display the door
rectangle(BROWN,585, 470, 90, 130)

# To display the doorknob
circle(BLACK,665,535,5)

# To display windows in house
rectangle(WINDOW_BLUE,750, 450, 100, 50)
circle(GREY,625,365,25)

# To display border lines of house
line(BLACK,625,300,825,300)
line(BLACK,550,400,625,300)
line(BLACK,625,300,700,400)
line(BLACK,550,400,900,400)
line(BLACK,825,300,900,400)
line(BLACK,550,400,550,600)
line(BLACK,700,400,700,600)
line(BLACK,900,400,900,600)
line(BLACK,550,600,900,600)
line(BLACK,585,470,585,600)
line(BLACK,585,470,675,470)
line(BLACK,675,470,675,600)
line(BLACK,750,450,850,450)
line(BLACK,750,475,850,475)
line(BLACK,750,500,850,500)
line(BLACK,750,450,750,500)
line(BLACK,850,450,850,500)
line(BLACK,800,450,800,500)
pygame.draw.circle(screen,BLACK,(625, 365),25,1)

# To display rooftop lines
line(BLACK,650,300,725,400)
line(BLACK,675,300,750,400)
line(BLACK,700,300,775,400)
line(BLACK,725,300,800,400)
line(BLACK,750,300,825,400)
line(BLACK,775,300,850,400)
line(BLACK,800,300,875,400)
line(BLACK,640,320,840,320)
line(BLACK,655,340,855,340)
line(BLACK,670,360,870,360)
line(BLACK,685,380,885,380)

# To display two trees at right and left random position
tx1=random.randint(60,110)
ty1=random.randint(300,360)
tree(tx1,ty1)
tx2=random.randint(950,970)
ty2=random.randint(275,360)
tree(tx2,ty2)

# To display two clouds at right and left random position
cx1=random.randint(20,120)
cy1=random.randint(50,100)
cloud(cx1,cy1)
cx2=random.randint(800,950)
cy2=random.randint(50,100)
cloud(cx2,cy2)

# To display ten random birds in the sky
bx1=random.randint(20,350)
by1=random.randint(20,70)
bird(bx1,by1)
bx=random.randint(20,350)
by1=random.randint(20,70)
bird(bx1,by1)
bx1=random.randint(20,350)
by1=random.randint(20,70)
bird(bx1,by1)
bx1=random.randint(20,350)
by1=random.randint(20,70)
bird(bx1,by1)
bx1=random.randint(20,350)
by1=random.randint(20,70)
bird(bx1,by1)
bx2=random.randint(600,950)
by2=random.randint(20,70)
bird(bx2,by2)
bx2=random.randint(600,950)
by2=random.randint(20,70)
bird(bx2,by2)
bx2=random.randint(600,950)
by2=random.randint(20,70)
bird(bx2,by2)
bx2=random.randint(600,950)
by2=random.randint(20,70)
bird(bx2,by2)
bx2=random.randint(600,950)
by2=random.randint(20,70)
bird(bx2,by2)


# To display random flower in the green field
fx1=random.randint(280,530)
fy1=random.randint(650,680)
flower(fx1,fy1)
fx1=random.randint(280,530)
fy1=random.randint(600,650)
flower(fx1,fy1)
fx1=random.randint(350,530)
fy1=random.randint(550,600)
flower(fx1,fy1)
fx1=random.randint(420,530)
fy1=random.randint(500,680)
flower(fx1,fy1)
fx1=random.randint(490,530)
fy1=random.randint(450,500)
flower(fx1,fy1)
fx1=random.randint(550,980)
fy1=random.randint(630,680)
flower(fx1,fy1)
fx1=random.randint(550,980)
fy1=random.randint(630,680)
flower(fx1,fy1)
fx1=random.randint(550,980)
fy1=random.randint(630,680)
flower(fx1,fy1)
fx1=random.randint(910,980)
fy1=random.randint(520,600)
flower(fx1,fy1)
fx1=random.randint(910,980)
fy1=random.randint(520,600)
flower(fx1,fy1)
fx1=random.randint(10,40)
fy1=random.randint(550,600)
flower(fx1,fy1)
fx1=random.randint(250,280)
fy1=random.randint(280,300)
flower(fx1,fy1)

# To display flowers on the bank of blue river
flower(40,620)
flower(70,590)
flower(100,555)
flower(130,520)
flower(160,485)
flower(190,450)
flower(220,425)
flower(250,390)
flower(280,355)
flower(310,320)
flower(340,285)
flower(550,275)
flower(520,310)
flower(490,345)
flower(460,380)
flower(430,415)
flower(405,450)
flower(380,485)
flower(355,520)
flower(330,555)
flower(305,590)
flower(280,625)
flower(255,660)


pygame.display.flip()
pygame.time.wait(20000) 
pygame.quit() 

