import pygame


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 900)) #Sets the size f the display in terms of number of pixels. Width, then height.
        self.clock = pygame.time.Clock() #Starts the gameclock, which sets the speed of the game.
        self.running = True #A variable we can use a switch to shut the game off if we need to.
        self.blocks = []
        self.players = []
        
    def main(self):
        while self.running: #Infinite loop. We will do these things over and over on repeat until our self.running variable gets set to False.
            self.events() #Check for any new events we need to act on
            self.update() #Update all of the things that move/change
            self.draw() #Redraw the screen, since things may have moved/changed.
            self.clock.tick(60) #60FPS. This just tells python to wait. The game is only allowed to execute this line 60 times per second.
            
    def events(self): #When called, Game checks if any input (clicking the x button, hitting a specific key, etc) needs acting on, and acts on it.
        for event in pygame.event.get(): #For each event pygame has as occuring...
            if event.type == pygame.QUIT: #If that event is the type of event that comes when the user hits the x button....
                self.running=False #Flips our switch to stop running the game. This closes the game, and the window.
                
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] == True:
            self.players[0].move('left')
        elif pressed[pygame.K_RIGHT] == True:
            self.players[0].move('right')
        elif pressed[pygame.K_UP] == True:
            self.players[0].move('up')
        elif pressed[pygame.K_DOWN] == True:
            self.players[0].move('down')
        
        if pressed[pygame.K_a] == True:
            self.players[1].move('left')
        elif pressed[pygame.K_d] == True:
            self.players[1].move('right')
        elif pressed[pygame.K_w] == True:
            self.players[1].move('up')
        elif pressed[pygame.K_s] == True:
            self.players[1].move('down')

            

            
    def update(self):
        pass

    def draw(self): #A method Games can do. It draws everything that should be on the screen to the screen, then updates the screen.
        self.screen.fill((0, 0, 0)) #black out the screen. This removes the last drawing we made, so we start with a fresh black canvas.
        for block in self.blocks:
            block.draw()
        for player in self.players:
            player.draw()
        pygame.display.update()

    def create(self):
        
        self.blocks.append(Block(200, 600, self))
        self.blocks.append(Block(500, 700, self))
        self.blocks.append(Block(250, 500, self))

        for px in range(0, 901, 30):
            self.blocks.append(Block(px, -30, self))
            self.blocks.append(Block(px, 900, self))
            self.blocks.append(Block(-30, px, self))
            self.blocks.append(Block(900, px, self))
        """
        self.blocks.append(Block(-30, 0, self))
        self.blocks.append(Block(30, -30, self))
        self.blocks.append(Block(-30, 30, self))
        self.blocks.append(Block(60, -30, self))
        self.blocks.append(Block(-30, 60, self))
        self.blocks.append(Block(90, -30, self))
        self.blocks.append(Block(-30, 90, self))
        self.blocks.append(Block(120, -30, self))
        self.blocks.append(Block(-30, 120, self))
        self.blocks.append(Block(150, -30, self))
        self.blocks.append(Block(-30, 150, self))
        self.blocks.append(Block(180, -30, self))
        self.blocks.append(Block(-30, 180, self))
        self.blocks.append(Block(210, -30, self))
        self.blocks.append(Block(-30, 210, self))
        self.blocks.append(Block(240, -30, self))
        self.blocks.append(Block(-30, 240, self))
        self.blocks.append(Block(270, -30, self))
        self.blocks.append(Block(-30, 270, self))
        self.blocks.append(Block(300, -30, self))
        self.blocks.append(Block(-30, 300, self))
        self.blocks.append(Block(330, -30, self))
        self.blocks.append(Block(-30, 330, self))
        self.blocks.append(Block(360, -30, self))
        self.blocks.append(Block(-30, 360, self))
        self.blocks.append(Block(390, -30, self))
        self.blocks.append(Block(-30, 390, self))
        self.blocks.append(Block(420, -30, self))
        self.blocks.append(Block(-30, 420, self))
        self.blocks.append(Block(450, -30, self))
        self.blocks.append(Block(-30, 450, self))
        self.blocks.append(Block(480, -30, self))
        self.blocks.append(Block(-30, 480, self))
        self.blocks.append(Block(480, -30, self))
        self.blocks.append(Block(-30, 480, self))
        self.blocks.append(Block(510, -30, self))
        self.blocks.append(Block(-30, 510, self))
        self.blocks.append(Block(510, -30, self))
        self.blocks.append(Block(-30, 510, self))
        self.blocks.append(Block(540, -30, self))
        self.blocks.append(Block(-30, 540, self))
        self.blocks.append(Block(570, -30, self))
        self.blocks.append(Block(-30, 570, self))
        self.blocks.append(Block(600, -30, self))
        self.blocks.append(Block(-30, 600, self))
        self.blocks.append(Block(630, -30, self))
        self.blocks.append(Block(-30, 630, self))
        self.blocks.append(Block(660, -30, self))
        self.blocks.append(Block(-30, 660, self))
        self.blocks.append(Block(690, -30, self))
        self.blocks.append(Block(-30, 690, self))
        self.blocks.append(Block(720, -30, self))
        self.blocks.append(Block(-30, 720, self))
        self.blocks.append(Block(750, -30, self))
        self.blocks.append(Block(-30, 750, self))
        self.blocks.append(Block(780, -30, self))
        self.blocks.append(Block(-30, 780, self))
        self.blocks.append(Block(810, -30, self))
        self.blocks.append(Block(-30, 810, self))
        self.blocks.append(Block(840, -30, self))
        self.blocks.append(Block(-30, 840, self))
        self.blocks.append(Block(870, -30, self))
        self.blocks.append(Block(-30, 870, self))
        self.blocks.append(Block(900, -30, self))
        self.blocks.append(Block(-30, 900, self))
        self.blocks.append(Block(900, 900, self))
        self.blocks.append(Block(870, 900, self))
        self.blocks.append(Block(840, 900, self))
        self.blocks.append(Block(810, 900, self))
        self.blocks.append(Block(780, 900, self))
        self.blocks.append(Block(750, 900, self))
        self.blocks.append(Block(720, 900, self))
        self.blocks.append(Block(690, 900, self))
        self.blocks.append(Block(630, 900, self))
        self.blocks.append(Block(600, 900, self))
        self.blocks.append(Block(570, 900, self))
        self.blocks.append(Block(540, 900, self))
        self.blocks.append(Block(510, 900, self))
        self.blocks.append(Block(480, 900, self))
        self.blocks.append(Block(450, 900, self))
        self.blocks.append(Block(420, 900, self))
        self.blocks.append(Block(390, 900, self))
        self.blocks.append(Block(360, 900, self))
        self.blocks.append(Block(330, 900, self))
        self.blocks.append(Block(300, 900, self))
        self.blocks.append(Block(270, 900, self))
        self.blocks.append(Block(240, 900, self))
        self.blocks.append(Block(210, 900, self))
        self.blocks.append(Block(180, 900, self))
        self.blocks.append(Block(150, 900, self))
        self.blocks.append(Block(120, 900, self))
        self.blocks.append(Block(90, 900, self))
        self.blocks.append(Block(60, 900, self))
        self.blocks.append(Block(30, 900, self))
        self.blocks.append(Block(900, 30, self))
        self.blocks.append(Block(900, 60, self))
        self.blocks.append(Block(900, 90, self))
        self.blocks.append(Block(900, 120, self))
        self.blocks.append(Block(900, 150, self))
        self.blocks.append(Block(900, 180, self))
        self.blocks.append(Block(900, 210, self))
        self.blocks.append(Block(900, 240, self))
        self.blocks.append(Block(900, 270, self))
        self.blocks.append(Block(900, 300, self))
        self.blocks.append(Block(900, 330, self))
        self.blocks.append(Block(900, 360, self))
        self.blocks.append(Block(900, 390, self))
        self.blocks.append(Block(900, 420, self))
        self.blocks.append(Block(900, 450, self))
        self.blocks.append(Block(900, 480, self))
        self.blocks.append(Block(900, 510, self))
        self.blocks.append(Block(900, 540, self))
        self.blocks.append(Block(900, 570, self))
        self.blocks.append(Block(900, 600, self))
        self.blocks.append(Block(900, 630, self))
        self.blocks.append(Block(900, 660, self))
        self.blocks.append(Block(900, 690, self))
        self.blocks.append(Block(900, 720, self))
        self.blocks.append(Block(900, 750, self))
        self.blocks.append(Block(900, 780, self))
        self.blocks.append(Block(900, 810, self))
        self.blocks.append(Block(900, 840, self))
        self.blocks.append(Block(900, 870, self))
        self.blocks.append(Block(900, 900, self))
        self.blocks.append(Block(900, 0, self))
        self.blocks.append(Block(900, 840, self))
        self.blocks.append(Block(900, 0, self))
        self.blocks.append(Block(900, 870, self))
        """


        self.players.append(Player(300, 300, self))
        self.players.append(Player(500, 500, self))
        
        
class Block:

    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 255, 0), pygame.Rect(self.x, self.y, 30, 30))

class Player:
    
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        self.speed = 3.2
        self.collide = 0
        self.collide2 = 5

    def draw(self):
        if self == self.game.players[0]: 
            pygame.draw.rect(self.game.screen, (0, 0, 255), pygame.Rect(self.x, self.y, 30, 30))
        if self == self.game.players[1]: 
            pygame.draw.circle(self.game.screen, (255, 0, 0), [self.x +15, self.y+15], 15)
        
    def move(self, direction):   
        if direction == 'left':
            self.x = self.x - self.speed
        if direction == 'right':
            self.x = self.x + self.speed
        if direction == 'up':
            self.y = self.y - self.speed
        if direction == 'down':
            self.y = self.y + self.speed

        if self.checkCollideBlock() == True:
            if direction == 'left':
                self.x = self.x + self.speed
            if direction == 'right':
                self.x = self.x - self.speed
            if direction == 'up':
                self.y = self.y + self.speed
            if direction == 'down':
                self.y = self.y - self.speed
            
        
        
    def checkCollideBlock(self):
        for block in self.game.blocks:
            collideX = block.x - 30 < self.x < block.x + 30
            collideY = block.y - 30 < self.y < block.y + 30
            if collideX and collideY: # if we are actually colliding
                return True
        return False

class Attack:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
    
    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 255), pygame.Rect(self.x, self.y, 30, 30))
        print ("hello")

#This is the code that gets executed when we tell python to run this file.
pygame.init() #Helps pygame start up, and sets up things like fonts
game = Game() #First, we make a Game object, calling its constructor. We save it to a variable so can access it later.
game.create() #We point to our game object and tell it to execute its create method. This builds the initial world and sets things up.
game.main() #We point to our game objecvt and tell it to execute its main method. This method contains an infinite loop and will continue to run while they are playing.
pygame.quit() #We can only make it to here if the infinite loop from main ended, which means we want to stop playing the game, so we quit.
