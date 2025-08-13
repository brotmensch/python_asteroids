import pygame
from constants import *

def main():

    pygame.init
    clock=pygame.time.Clock()
    dt=0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    i=0
    while i==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt=clock.tick(60)/1000
        
    
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
