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
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
    
    def say(self):
        print("안녕하세요, 내 이름은 {}이고, 내 나이는 {}입니다.".format(self.name, self.age))

    def set_pos(self, pos):
        self.pos = pos


class GameMain():
    done = False
    debug = False
    color_gray = Color('lightgray')
    mans = []

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
        for one in self.mans:
            new_x = one.pos[0] + one.speed_x
            new_y = one.pos[1] + one.speed_y
            one.pos = (new_x, new_y)


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
                    age = random.randint(20, 100)
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
            r = Rect(one.pos[0], one.pos[1], one.width, one.height) 
            self.screen.fill(one.color, r) 

        # will call update on whole screen Or flip buffer.
        pygame.display.flip()

    
if __name__ == '__main__':
    g = GameMain()
    g.loop()
    pygame.quit()
    #sys.exit()
