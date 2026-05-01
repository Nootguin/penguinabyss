import pygame
from os import path

# Images directory
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

# Window
WIDTH = 480
HEIGHT = 600
FPS = 60

# Colours
WHITE = ("#FFFFFF")
BLACK = ("#000000")
SEA =("#3A72AE")

# Initialise pygame and create the window
pygame.init() # runs pygame
pygame.mixer.init() # initalises sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("oop4") # Sets Window Name
clock = pygame.time.Clock() # clock is a part of time and time is part of pygame

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 500
        self.speedx = 0 # speedx property that will keep track of how fast the player is moving in the x direction (side-to-side).
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Start Game
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(SEA)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
pygame.quit()