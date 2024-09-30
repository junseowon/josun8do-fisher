import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption("조선 팔도 어부")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

white = (255,255,255) 
red = (255,0,0) 
green = (0,255,0) 

textFont = pygame.font.Font("./Fonts/font_kdg/솔뫼 김대건 Light.ttf", 125)

mainScene = pygame.transform.scale(pygame.image.load("./Images/Background/game_Background.png"), (1600, 900))
mainTitle = pygame.transform.scale(pygame.image.load("./Images/Background/game_title.png"), (800, 320))
mainScene_y = -1000
finishSceneOpen = False

mainBGM = pygame.mixer.Sound( "./Sounds/BGM/main_title_BGM.mp3" )
mainBGM.set_volume(0.1)
mainBGM.play(-1)

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mainScene_y <= 0 and not finishSceneOpen:
        mainScene_y += 600 * dt
    else:
        mainScene_y = 0
        finishSceneOpen = True

    screen.blit(mainScene, (0, 0))
    screen.blit(mainTitle, (500, mainScene_y))
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
