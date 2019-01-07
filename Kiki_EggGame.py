import pygame
import random
import tkinter as tk
from tkinter import messagebox
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Kiki's Egg Catcher!")
clock = pygame.time.Clock()
chicken = [(75, 100, 15, 20),(130, 150, 15, 20),(360, 150, 15, 20),(415, 100, 15, 20)]
basket = []
class eggs(object):
    
    def __init__(self,x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
    def draw(self, window):
        pygame.draw.ellipse(window, (225,255,255), [self.x, self.y, self.width, self.height])
        
    def fall(self, window):
        self.y+=self.vel
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
    def draw(self, window):
        kiki_png = pygame.image.load("kiki.png")
        window.blit(kiki_png, (self.x, self.y))
        self.hitbox = (self.x,self.y, self.width,self.height-5)
        pygame.draw.rect(window,(255,0,0),self.hitbox,1) 


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass         
    
    
def drawWindow(window, chicken):
    text = font.render('Score: ' + str(score), 1, (255,255,255))
    window.blit(text, (200,10))
    kiki.draw(window)
    chicken_1 = pygame.image.load("chicken.png")
    chicken_2 = pygame.image.load("chicken.png")
    chicken_3 = pygame.image.load("chicken.png")
    chicken_4 = pygame.image.load("chicken.png")
    window.blit(chicken_1, (chicken[0][0]-30, chicken[0][1]-10))
    window.blit(chicken_2, (chicken[1][0]-30, chicken[1][1]-20))        #100, 150
    window.blit(chicken_3, (chicken[2][0]-30, chicken[2][1]-20))
    window.blit(chicken_4, (chicken[3][0]-30, chicken[3][1]-10))
    pygame.draw.line(window,(255,255,255),(0,450),(500, 450))
run = True
broken_bool = False
counter = 0
kiki = player(250, 355, 64,101)
CD = 35
broken = []
score = 0
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
font = pygame.font.SysFont('comicsans',30,True)
while run:
    
    window.fill((0,0,0))
    #pygame.time.delay(150)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    clock.tick(60)
    #-----player move--------#
    counter+=1
    if keys[pygame.K_LEFT]:
        kiki.x = kiki.x -kiki.vel
    if keys[pygame.K_RIGHT]:
        kiki.x=kiki.x+kiki.vel
    #----------------------------------------------------------------end move player-----
    
    #select chicken--------------------------
    random_int = random.randint(0, 3)    
    if (len(basket)<6 and counter == CD):
        basket.append(eggs(chicken[random_int][0],chicken[random_int][1],chicken[random_int][2],chicken[random_int][3]))
        counter =0
    elif(counter >= CD):
        counter = CD-1
        #print(basket)
#---Draw----------------------------#

    #Check if dropped eggs----------------------------------------------#
    for egg in basket:
        egg.fall(window)
        if(egg.y + egg.height<450):
            #check if caught-----------------------------#
            if(egg.x+egg.width>kiki.x and egg.x <kiki.x+ kiki.width and egg.y <kiki.y+kiki.height and egg.y+egg.height> kiki.y):
                score+=1
                basket.pop(basket.index(egg))
                broken_bool = True
            egg.draw(window)
        else:
            basket.pop(basket.index(egg))
            score-=1
            #broken_bool = True
            
    if(score < -1):
        message_box('You Lost!', 'Play again...')
        pygame.quit()
        
    
    drawWindow(window,chicken)
    pygame.display.update()
pygame.quit()


























