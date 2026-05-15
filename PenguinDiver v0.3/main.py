# Penguin Diver - platformer game
import pygame as pg
import random
from settings import *
from sprites import *


class Game:
    def __init__(self): # Initalises the game window
        pg.init() # runs pygame
        pg.mixer.init() # initalises sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE) # Sets Window Name
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self): # Starts a fresh game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()
    
    def run(self): # Runs the game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self): # Updates within the game loop
        self.all_sprites.update()

    def events(self): # Events within the game loop
        for event in pg.event.get(): # enables closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            
    def draw(self): # Everything drawn within the game loop
        # Draw / render
        self.screen.fill(SEA)
        self.all_sprites.draw(self.screen)       
        pg.display.flip() # after drawing everything, flip the display

    def start_screen(self): 
        pass

    def game_over_screen(self):
        pass


game = Game()
game.start_screen()
while game.running:
    game.new()
    game.game_over_screen()
pg.quit()


    