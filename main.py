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

myTextFont = pygame.font.Font("./Fonts/font_kdg/솔뫼 김대건 Light.ttf", 125)
myText = myTextFont.render("조선 팔도 어부", True, red) 
myTextArea = myText.get_rect() 
myTextArea.center = (player_pos.x, player_pos.y - 300)

IntroScreen = pygame.transform.scale(pygame.image.load('./Images/Background/game_intro.jpg'), (1600, 900))

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    
    screen.blit(IntroScreen, (0, 0)) 
    
    screen.blit(myText, myTextArea) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
