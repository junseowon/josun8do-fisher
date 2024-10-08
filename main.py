import pygame
import game
import fade
import math
import random

def DisplayText(surface, center_x, center_y, font_path, font_size, text, anti_aliasing, color):    
    textFont = pygame.font.Font(font_path, font_size)
    
    text_contents = textFont.render(text, anti_aliasing, color)
    text_contents_rect = text_contents.get_rect()    
    text_contents_rect.center = (center_x, center_y)

    surface.blit(text_contents, text_contents_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    center_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    clock = pygame.time.Clock()

    running = True
    dt = 0

    WHITE = (255, 255, 255)
    DARK_BLUE = (0, 0, 128)
    LIGHT_BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    pygame.display.set_caption("조선 팔도 어부")

    mainScene = pygame.transform.scale(pygame.image.load("./Images/Background/game_Background.png"), (1600 * 1.1, 900 * 1.1))
    mainTitle = pygame.transform.scale(pygame.image.load("./Images/Background/game_title.png"), (800, 320))
    mainScene_y = -1000
    finishSceneOpen = False

    mainBGM = pygame.mixer.Sound( "./Sounds/BGM/main_title_BGM.mp3" )
    waveBGM = pygame.mixer.Sound( "./Sounds/BGM/waves_BGM.mp3" )

    mainBGM.set_volume(0.1)
    mainBGM.play(-1)

    waveBGM.set_volume(0.1)
    waveBGM.play(-1)

    button_image = pygame.image.load('./Images/UI/start_btn.png')  # 버튼 이미지 파일 경로 설정

    button_rect = button_image.get_rect()  # 이미지의 Rect 정보 얻기
    button_rect.center = (center_pos.x + 20, center_pos.y + 300)  # 버튼 위치 설정

    original_size = button_image.get_size()  # 원래 이미지 크기 확인
    new_size = (int(original_size[0] * 1.1), int(original_size[1] * 1.1))
    scaled_button_image = pygame.transform.scale(button_image, new_size)

    button_hover_rect = scaled_button_image.get_rect()  # 이미지의 Rect 정보 얻기
    button_hover_rect.center = (center_pos.x + 20, center_pos.y + 300)  # 버튼 위치 설정

    radius = 5  # 원의 반지름
    angle = 0  # 초기 각도
    while running:

        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
                    
        if mainScene_y <= 0 and not finishSceneOpen:
            mainScene_y += 600 * dt
        else:
            mainScene_y = 0
            finishSceneOpen = True

        # 각도를 증가시키며 원형 경로를 계산
        if finishSceneOpen:      
            angle += random.randint(1, 5) * dt   # 각도를 천천히 증가시킴 (속도 조정 가능)

        # 원형 경로상의 X, Y 좌표 계산
        x = center_pos.x + math.cos(angle) * radius  # 코사인으로 X 좌표 계산
        y = center_pos.y + math.sin(angle) * radius  # 사인으로 Y 좌표 계산
        # 이미지 그리기 (새로운 좌표에 이미지 배치)
        mainScene_rect = mainScene.get_rect(center=(x, y))
        screen.blit(mainScene, mainScene_rect)
        
        screen.blit(mainTitle, (500, mainScene_y))

        if finishSceneOpen:        
            if button_rect.collidepoint(mouse):
                screen.blit(scaled_button_image, button_hover_rect)  # 마우스가 버튼 위에 있으면 hover 이미지 표시
                DisplayText(screen, center_pos.x, center_pos.y + 280,
                            "./Fonts/font_kdg/솔뫼 김대건 Light.ttf", 77, '시작하기', False, WHITE)        
                if click[0] == 1:  # 마우스 왼쪽 클릭                    
                    if fade.In(screen, BLACK, 1, 0):
                        game.Play(screen, screen.get_width(), screen.get_height())
                        break
            else:
                screen.blit(button_image, button_rect)  # 기본 버튼 이미지 표시
                DisplayText(screen, center_pos.x, center_pos.y + 280,
                            "./Fonts/font_kdg/솔뫼 김대건 Light.ttf", 70, '시작하기', False, WHITE)        
                            
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

