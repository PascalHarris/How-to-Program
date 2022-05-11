import pygame

# Constants
BULLET_DELAY = 1000 # 1000ms = 1s
MOVE_DIST = 5 # distance moved for each key press

# Classes
class Sprite(object):
    def __init__(self, xpos, ypos, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=xpos, y=ypos)
    
    def current_position(self): 
        return self.rect
    
    def draw(self, surface): 
        surface.blit(self.image, self.rect)
    
class Bullet(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos, "Missile.bmp") 
        # change position
        self.rect.centerx = xpos
        self.rect.bottom = ypos

class Alien(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos, "Alien.bmp") 

class Player(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos, "Spaceship.bmp") 
        # change position
        self.rect.centerx = xpos
        self.rect.bottom = ypos

# The main program
pygame.init()
screen = pygame.display.set_mode((640, 480)) 
screen_rect = screen.get_rect()
player = Player(screen_rect.centerx, screen_rect.bottom) # create player sprite 
missiles = [] # create missile array

# layout the initial field of aliens 
aliensW = 6
aliensH = 3
sx = screen_rect.width/7
sy = screen_rect.width/7
aliens = [[Alien(sx*(x+0.75),sy*(y+0.5)) for x in range(aliensW)] for y in range(aliensH)]

# move direction 
move_left = False
current_time = pygame.time.get_ticks()

# missile delay 
next_missile_time = current_time

clock = pygame.time.Clock() 
running = True

while running: # the event loop
    current_time = pygame.time.get_ticks()
    
    # events (it's called an event loop for a reason!) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: # right key 
        player.rect.x += MOVE_DIST
        if player.rect.right > screen_rect.right:
            player.rect.right = screen_rect.right
            
    if key[pygame.K_LEFT]: # left key 
        player.rect.x -= MOVE_DIST
        if player.rect.left < screen_rect.left:
            player.rect.left = screen_rect.left
    
    if key[pygame.K_SPACE]: # fire key
        if current_time >= next_missile_time:
            missiles.append(Bullet(player.rect.centerx, player.rect.top))
            next_missile_time = current_time + BULLET_DELAY #delay before next missile is shot
    
    # move missiles (and remove if leaves screen) 
    temp = []
    for m in missiles:
        m.rect.y -= MOVE_DIST 
        if m.rect.bottom >= 0:
            temp.append(m) 
    missiles = temp
    
    # move aliens (and check if a missile hits) 
    temp = []
    next_direction = move_left
    for row in aliens:
        temp_row = [] 
        for a in row:
            if move_left: # move
                a.rect.x -= 1
                # check collision
                for i, m in enumerate(missiles):
                    if a.rect.colliderect(m.rect): 
                        # remove missile
                        del missiles[i]
                        # don't check for collisions with other missiles 
                        break
                    else: # check only if loop hasn't encountered "break" (no collision)
                    # check if direction is required
                    if a.rect.left == screen_rect.left:
                    # need to change direction but don't change `move_left` yet
                        next_direction = False 
                    temp_row.append(a)
            else:
                # move
                a.rect.x += 1
                # check collision
                for i, m in enumerate(missiles):
                    if a.rect.colliderect(m.rect): 
                        # remove missile
                        del missiles[i]
                        # don't check for collisions with other missiles 
                        break
                else: # check only if loop hasn't encountered "break" (no collision)
                    if a.rect.right == screen_rect.right: 
                    # need to change direction 
                        next_direction = True
                    temp_row.append(a) 
        temp.append(temp_row)
    
    move_left = next_direction
    
    # new list without destroyed aliens 
    aliens = temp
    
    # redraw screen
    screen.fill((255, 255, 255)) # fill the screen with white - without this the old graphics will remain onscreen.
    
    for row in aliens: 
        for a in row:
            a.draw(screen) 
    
    for m in missiles:
        m.draw(screen)
    
    player.draw(screen) # draw the spaceship to the screen 
    pygame.display.update() # update the screen
    clock.tick(40) # 40 is the number of fps1 that the game will play at