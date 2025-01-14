import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))

        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            if a.checkCollision(player):
                print("GAME OVER!")
                exit()
            for s in shots:
                if a.checkCollision(s):
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        loopTime = clock.tick(60)
        dt = loopTime / 1000

if __name__ == "__main__":
    main()