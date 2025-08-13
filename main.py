import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    

    pygame.init()
    clock=pygame.time.Clock()
    dt=0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    asteroids=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(updatable, drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots, updatable,drawable)
    asteroidfield=AsteroidField()
    player=Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    
   
   
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for object in asteroids:
            if object.collides_with(player):
                print("Game over!")
                sys.exit()
        for object in asteroids:
            for shot in shots:
                if shot.collides_with(object):
                    shot.kill()
                    object.kill()

        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        
        
        pygame.display.flip()
       
        dt=clock.tick(60)/1000
        
    
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
