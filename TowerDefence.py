
import pygame

pygame.init()

GameDisplay = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("타워 디펜스")

## 그림모음집 ##
background1 = pygame.image.load("C:/Users/B760I/Desktop/hanyang projact/대충 개쩌는 배경.png")
background2 = pygame.image.load("C:/Users/B760I/Desktop/hanyang projact/대충 개쩌는 메인화면.png")
font = pygame.font.Font(None,100)
start = font.render(str("Press ENTER to start!!"), True, (0,0,0))
gamepage = 0 ## gamepage
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if gamepage == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gamepage+=1
                
    if gamepage == 0:
        GameDisplay.blit(background1,(0,0))
        GameDisplay.blit(start,(550,490))
        
        

    if gamepage == 1:
        GameDisplay.blit(background2,(0,0))


    pygame.display.update()


pygame.quit()
