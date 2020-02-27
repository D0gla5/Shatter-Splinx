import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
from shatterSplinx import ShatterSplinx

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Shatter splinx"
# pixels width
WINDOW_WIDTH  = 800
# pixels high
WINDOW_HEIGHT = 800
# frames per second
DESIRED_RATE  = 60

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        self.title = title
        self.width = width
        self.height = height
        self.frameRate = frame_rate
        
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = ShatterSplinx(width, height)
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

        if pygame.K_SPACE in newkeys:
             if self.mGame.circle.getDistance(self.mGame.circle2) < 100:
                 self.mGame.circle, self.mGame.circle2 = self.mGame.makeRandomShapes()
                
        
        self.mGame.update()

        return
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        pygame.draw.rect(surface, (255,255,255), (0,0,self.width,self.height))
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
