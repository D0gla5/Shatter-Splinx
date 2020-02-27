import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
from asteroids import Asteroids

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "ASTEROIDS"
# pixels width
WINDOW_WIDTH  = 900
# pixels high
WINDOW_HEIGHT = 900
# frames per second
DESIRED_RATE  = 20

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        self.title = title
        self.width = width
        self.height = height
        self.frameRate = frame_rate
        
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = Asteroids(width, height)
        self.startUpTime = pygame.time.get_ticks()
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # keys contains all keys currently held down
        # newkeys contains all keys pressed since the last frame
        # Use pygame.K_? as the keyboard keys.
        # Examples: pygame.K_a, pygame.K_UP, etc.
        # if pygame.K_UP in newkeys:
        #    The user just pressed the UP key
        #
        # buttons contains all mouse buttons currently held down
        # newbuttons contains all buttons pressed since the last frame
        # Use 1, 2, 3 as the mouse buttons
        # if 3 in buttons:
        #    The user is holding down the right mouse button
        #
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame
        
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        if pygame.K_LEFT in keys:
            self.mGame.turnShipLeft(20)
        elif pygame.K_RIGHT in keys:
            self.mGame.turnShipRight(20)
        
        if pygame.K_UP in keys:
            self.mGame.accelerateShip(10)

        if pygame.K_SPACE in newkeys:
            self.mGame.fire()

        if pygame.K_r in newkeys:
            self.__init__(self.title, self.width, self.height, self.frameRate)

        self.mGame.evolve( dt )
        timeSeconds = (pygame.time.get_ticks()-self.startUpTime)/1000
        if not self.mGame.timerStopped():
            time = str(timeSeconds)
            milis = time[time.index("."):]
            seconds = time[:time.index(".")]
            while len(milis) < 4:
                milis = milis + "0"
            self.mGame.setTimer(seconds+milis)

        return
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        pygame.draw.rect(surface, (0,0,0), (0,0,self.width, self.height), 0)
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
