encoding='utf-8'
import pygame , sys
pygame.init()
from pygame.locals import*  # sare module ko import krta h
import random
import math
import time
screen=pygame.display.set_mode((620,700)) # screen size in which game display
pygame.mixer.init()
pygame.display.set_caption("RACING CAR") # title of game
# countdown time
def countdown(t):
    countdownBackground=pygame.image.load('myrd.jpeg')
 # displaying 1 2 3
    screen.blit(countdownBackground,(0,0))
    pygame.display.update()
    time.sleep(0.8)
    screen.blit(t,(280,450))
    pygame.display.update()
    time.sleep(0.8)
    pygame.display.update()
font2=pygame.font.Font('FreeSansBold.ttf',70)
t1=font2.render('3',True,(187,30,40))
t2=font2.render('2',True,(187,30,40))
t3=font2.render('1',True,(187,30,40))
t4=font2.render('GO',True,(187,30,40))
for i in (t1,t2,t3,t4):
   countdown(i)

class background:
    def __init__(self):
        self.bg=pygame.image.load('myrd.jpeg')
        self.y, self.speed= -500,0
    def draw(self):
        self.y+=self.speed
        if self.p>=0:
            self.y=-500
            screen.blit(self.bg,(0,int(self.y)))


def gameloop():
    pygame.mixer.music.load('bgmusic.mp3')
    pygame.mixer.music.play(-1)
    crash_sound=pygame.mixer.Sound('crashsound.mpeg')
    #scoring boards
    font1=pygame.font.Font("FreeSansBold.ttf",25)
    score_value=0
    def _score_(x,y):
        score=font1.render("SCORE: "+str(score_value),True,(255,0,0))
        screen.blit(score,(x,y))
    
# adding game over image
    def gameover():
        img=pygame.image.load('gameover.png')
        run=True
        while run:
            screen.blit(img,(30,190))
            time.sleep(0.2)
            _score_(330,400)
            time.sleep(0.4)
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        countdown(i)
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    

   
    bg=pygame.image.load('myrd.jpeg')
    
    mycar=pygame.image.load('car5.jpeg')
    mycarX=250
    mycarY=600
    inx=0
    iny=0
    # others players
    c1=pygame.image.load('car4.jpeg')
    c1x=random.randint(100,200)
    c1y=2
    c_y1=2
    c2=pygame.image.load('car2.jpeg')
    c2x=random.randint(150,350)
    c2y=2
    c_y2=4
    c3=pygame.image.load('car3.jpeg')
    c3x=random.randint(300,500)
    c3y=2
    c_y3=3


    run=True
    while (run):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # key daba ke baad
                if event.key==pygame.K_RIGHT:
                    inx+=5
                if event.key==pygame.K_LEFT:
                    inx-=5
                if event.key==pygame.K_UP:
                    iny-=5
                if event.key==pygame.K_DOWN:
                    iny+=5
            if event.type == pygame.KEYUP: # key chorne ke baad
                if event.key==pygame.K_RIGHT:
                    inx=0
                if event.key==pygame.K_LEFT:
                    inx=0
                if event.key==pygame.K_UP:
                    iny=0
                if event.key==pygame.K_DOWN:
                    iny=0

        # setting boundary for my car
        if mycarX<130:
            mycarX=130
        if mycarX>500:
            mycarX=500
        if mycarY<0:
            mycarY=0
        if mycarY>500:
            mycarY=500



        screen.fill((0,0,0)) # n color is fill
        screen.blit(bg,(0,0))
            
        # displaying all crs
        screen.blit(mycar,(mycarX,mycarY))
        screen.blit(c1,(c1x,c1y))
        screen.blit(c2,(c2x,c2y))
        screen.blit(c3,(c3x,c3y))
        # calling our score_value and hghscore func
        _score_(500,70)

        # updating my car coordiate
        mycarX+=inx
        mycarY+=iny
        c1y+=c_y1
        c2y+=c_y2
        c3y+=c_y3
        # moving of enemies car in infinite loop
        if c1y>700:
            c1y=-150
            score_value+=1
        if c2y>690:
            c2y=-150
            score_value+=1
        if c3y>690:
            c3y=-150
            score_value+=1
        # background
        
        # checkng collision
        def collisions(x1,y1,x,y):
            d=math.sqrt(math.pow(x1-x,2)+math.pow(y1-y,2))
            if d<42:
                return True
            else:
                return False
        collision1=collisions(c1x,c1y,mycarX,mycarY)
        collision2=collisions(c2x,c2y,mycarX,mycarY)
        collision3=collisions(c3x,c3y,mycarX,mycarY)
    
        if collision1:
            screen.fill((0,0,0))
            c_y1=0
            c_y2=0
            c_y3=0
            inx=0
            iny=0
            pygame.mixer.music.stop()
            crash_sound.play()
            gameover()
        if collision2:
            screen.fill((0,0,0))
            c_y1=0
            c_y2=0
            c_y3=0
            inx=0
            iny=0
            pygame.mixer.music.stop()
            crash_sound.play()
            gameover()
        if collision3:
            screen.fill((0,0,0))
            c_y1=0
            c_y2=0
            c_y3=0
            inx=0
            iny=0
            pygame.mixer.music.stop()
            crash_sound.play()
            gameover()
        
        pygame.display.update()

gameloop()


