import pygame
from pygame.locals import *
from pygame import Color, Rect
import sys
import math
import random

name_list = ['ato', 'john', 'smith', 'kendo', 'young', 'yujin', 'mee', 'yaker']

class person():
    def __init__(self, name, age):
        self.width = random.randint(5, 10)
        self.height = random.randint(8, 16)
        self.color = Color( random.randint(50, 255), random.randint(50, 255), random.randint(50, 255) )
        self.name = name
        self.age = age
        self.blink = False
        self.visible = True
        self.flowcount = 0
        self.growup_speed = 1
        rx = random.randint(-2, 2)
        self.speed_x = 0.2 if rx == 0 else rx
        ry = random.randint(-2, 2)
        self.speed_y = 0.2 if ry == 0 else ry
    
    def say(self):
        #print("안녕하세요, 내 이름은 {}이고, 내 나이는 {}입니다.".format(self.name, self.age))
        self.msg = self.name + " " + str(self.age) 

    def update(self):
        x = self.pos[0] + self.speed_x
        y = self.pos[1] + self.speed_y
        self.pos = (x, y)

        self.check_edge()
        self.say()
        if( self.flowcount % 60 == 0 ):
            self.growup()
            self.flowcount = 0

        if self.age >= 80 :
            if self.flowcount % 20 == 0 :
                self.visible  = ( self.visible == False )
        else: 
            self.visible = True
            

        self.flowcount += self.growup_speed
        

    def set_pos(self, pos):
        self.pos = pos

    def growup(self):
        self.age += 1

    def check_edge(self):
        if self.pos[0] < 0 or self.pos[0] > 800:
            self.speed_x *= -1
        if self.pos[1] < 0 or self.pos[1] > 600:
            self.speed_y *= -1

    def set_blink(self):
        if self.age >= 100:
            self.blink = True

class GameMain():
    done = False
    debug = False
    color_gray = Color('lightgray')
    mans = []
    young = 0
    adult = 0
    old = 0

    def __init__(self, width=800, height=600, color_bg=None):
        """Initialize PyGame"""
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Person : pygame")

        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.limit_fps_max = 60

        if color_bg is None:
            color_bg = Color(50, 50, 50)
        self.color_bg = color_bg

        self.game_init()

    def game_init(self):
        """new game/round"""
        self.mans = []
        self.count = 0
        self.game_font = pygame.font.Font( pygame.font.get_default_font(), 12)
        self.game_font_large = pygame.font.Font( pygame.font.get_default_font(), 24)

    def loop(self):
        """Game() main loop"""
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

            if self.limit_fps:
                self.clock.tick(self.limit_fps_max)
            else:
                self.clock.tick()
            
            self.count += 1

    def update(self):
        self.young = self.adult = self.old = 0

        for one in self.mans:
            if one.age < 10:
                self.young += 1
            elif one.age < 40:
                self.adult += 1
            else:
                self.old += 1 
            
            one.update()

            if one.age > 100:
                self.mans.remove(one)
                self.old -= 1


    def handle_events(self):
        """handle regular events. """
        events = pygame.event.get()
        # kmods = pygame.key.get_mods() # key modifiers
        try:
            for event in events:
                if event.type == pygame.QUIT:
                    # Sould set to the self.done = False!!! and call sys.exit() 
                    self.done = True
                    pygame.quit()
                    #sys.exit()
                    
                elif event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        self.done = True
                        break
                    elif (event.key == K_SPACE):
                        self.game_init()
                elif event.type == MOUSEBUTTONUP and event.button == 1 :
                    pos = pygame.mouse.get_pos()
                    #self.circles.append( Circle(pos, 6))
                    name = random.sample(name_list, 1)[0]
                    age = random.randint(2, 100)
                    p = person(name, age)
                    p.set_pos(pos)
                    self.mans.append( p )
        finally:
            pass

    def draw(self):
        """render screen"""
        if self.done :
            return

        # clear screen
        self.screen.fill(self.color_bg)

        # mans: draw
        for one in self.mans:
            if one.visible == True:
                r = Rect(one.pos[0], one.pos[1], one.width, one.height) 
                self.screen.fill(one.color, r) 
                t_view = self.game_font.render(one.msg, True, one.color)
                t_rect = t_view.get_rect()
                t_rect.topleft = (one.pos[0], one.pos[1]-12)
                self.screen.blit(t_view, t_rect)

        score = "Total:{}, Y:{}, A:{}, O:{}".format(self.young + self.adult + self.old, self.young, self.adult, self.old)
        t_view = self.game_font_large.render(score, True, Color(255, 255, 255))
        t_rect = t_view.get_rect()
        t_rect.topleft = (10, 10)
        self.screen.blit(t_view, t_rect)

        # will call update on whole screen Or flip buffer.
        pygame.display.flip()
    

if __name__ == '__main__':
    g = GameMain()
    g.loop()
    pygame.quit()
    #sys.exit()
