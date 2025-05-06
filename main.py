# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField


def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable, )
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
  asteroid_field = AsteroidField()
  
  dt = 0
  
  while True:
   dt = clock.tick(60) / 1000
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
   
   screen.fill("black")
   for obj in drawable:
    obj.draw(screen)
    
   updatable.update(dt)

   
   
   pygame.display.flip()


if __name__ == "__main__":
   main()