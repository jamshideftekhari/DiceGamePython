import sys, pygame, DieGame
from pygame.constants import GL_ACCELERATED_VISUAL

pygame.init()

size = width, height = 240, 260
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
fillColor=black
fv1=str(0)
fv2=str(0)
Dg = DieGame.DieGame()
screen = pygame.display.set_mode(size)
while 1: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_SPACE: 
              Dg.Play()
              fv1=str(Dg.GetResult())
              if fv1=="7": fillColor = green
              else: fillColor = black
              
    screen.fill(fillColor)
    rect=(70,20,100,100)
    font = pygame.font.SysFont(None,64)
    image = font.render(fv1, True, black)
    pygame.draw.rect(screen, white, rect) 
    screen.blit(image, (100, 50))
    rect=(70,140,100,100)
    pygame.draw.rect(screen, white, rect)
    image = font.render(fv2, True, black)   
    screen.blit(image, (100, 170)) 
            
    pygame.display.update()    
            