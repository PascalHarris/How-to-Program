import pygame
class Player(object):
    def __init__(self, screen):
        self.image = pygame.image.load("Spaceship.bmp") # load spaceship image 
        self.rect = self.image.get_rect() # get size of spaceship 
        size = screen.get_rect()
        # draw the spaceship in the horizontal middle
        self.x = (size.width * 0.5) - (self.rect.width * 0.5) 
        # draw the spaceship at the bottom
        self.y = size.height - self.rect.height
    
    def current_position(self): 
        return self.x
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y)) # blit to player position
    
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
counter = 0 # Counter to prove that the event loop runs between key presses 
player = Player(screen) # create the player sprite
running = True

while running: # the event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    dist = 1                  # distance moved for each key press 
    if key[pygame.K_RIGHT]:   # right key
        player.x += dist 
    elif key[pygame.K_LEFT]:  # left key
        player.x -= dist
    
   
    screen.fill((255, 255, 255)) # fill the screen with white 
    player.draw(screen)          # draw the spaceship to the screen 
    pygame.display.update()      # update the screen
    clock.tick(40)
    
    counter+=1 
    print (counter)