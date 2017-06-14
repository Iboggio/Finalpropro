"""
 Show how to fire bullets.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/PpdJjaiLX6A
"""
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BURGUNDY = (140, 0, 26)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
 
# --- Classes
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image = pygame.transform.scale(pygame.image.load("alien.bmp").convert(), (30,30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("player.bmp").convert(), (30,30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
        self.rect.y = 350 
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BURGUNDY)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(50):
    # This represents a block
    block = Block(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(300)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)

#load the sound
sound = pygame.mixer.Sound("bomb-02.ogg")
sound2 = pygame.mixer.Sound("laser5.ogg") 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 370
start_ticks=pygame.time.get_ticks() #starter tick

file = open('highscores.txt', 'r')
except:
    file = open('highscores.txt', 'w')
    file.write("Empty\n0\nEmpty\n0\nEmpty\n0\nEmpty\n0\nEmpty\n0")
    file.close()
    file = open('highscores.txt', 'r')
finally:
    iterate = 0
    highscore_list = []
    name_list = []
    for line in file:
        iterate += 1
        if iterate % 2 == 0:
            highscore_list.append(line)
        else: 
            name_list.append(line)
    file.close()

# Clean up the lists containing the names and the scores
for i in range(len(highscore_list)):
    highscore_list[i].replace("\n", "")
    highscore_list[i] = int(highscore_list[i])
    
for i in range(len(name_list)):
    name_list[i] = name_list[i].replace("\n", "")

 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            sound2.play()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x+12
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds>15: # if more than 10 seconds close the game
        done = True
          
       
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        
        
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            sound.play()
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
        if score > 50:
            done = True
            
        if done = True:
                for i in range(5):
                    if not score > int(highscore_list[i]):
                        continue
                    else:
                        highscore_list.insert(i, score)
                        name_list.insert(i, name)
                        break
                with open('highscores.txt', 'w') as file:
                    for i in range(5):
                        file.write(str(name_list[i]) + "\n")
                        file.write(str(highscore_list[i]) + "\n")        
        
 
    # --- Draw a frame
 
    # Clear the screen
    screen.fill(BLACK)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()