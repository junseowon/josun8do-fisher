import pygame
import sys

def Play(screen, screen_width, screen_height):
    # 파이게임 초기화
    pygame.init()

    # 색상 정의 (RGB)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)

    # 폰트 설정
    font = pygame.font.SysFont(None, 40)

    # 팝업창 상태
    popup_active = False

    # 팝업창 그리기 함수
    def draw_popup(screen):
        # 팝업창 배경
        popup_width = 400
        popup_height = 300
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2
        pygame.draw.rect(screen, GREY, (popup_x, popup_y, popup_width, popup_height))
        
        # 팝업창 테두리
        pygame.draw.rect(screen, BLACK, (popup_x, popup_y, popup_width, popup_height), 5)
        
        # 팝업창 텍스트
        text = font.render('This is a popup window!', True, BLACK)
        screen.blit(text, (popup_x + 50, popup_y + 100))

        # 버튼 그리기
        button_width = 100
        button_height = 50
        button_x = popup_x + (popup_width - button_width) // 2
        button_y = popup_y + popup_height - 80
        pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))
        
        button_text = font.render('Close', True, WHITE)
        screen.blit(button_text, (button_x + 10, button_y + 10))

    # 메인 루프
    running = True
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # 'P' 키로 팝업창 열기/닫기
                    popup_active = not popup_active
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if popup_active:
                    # 마우스 클릭 좌표
                    mouse_x, mouse_y = event.pos
                    # 팝업창 닫기 버튼 클릭 처리
                    popup_x = (screen_width - 400) // 2
                    popup_y = (screen_height - 300) // 2
                    button_x = popup_x + 150
                    button_y = popup_y + 220
                    if button_x <= mouse_x <= button_x + 100 and button_y <= mouse_y <= button_y + 50:
                        popup_active = False

        # 화면 채우기
        screen.fill(WHITE)

        # 팝업창이 활성화되어 있으면 그리기
        if popup_active:
            draw_popup(screen)

        # 화면 업데이트
        pygame.display.update()

    # 파이게임 종료
    pygame.quit()
    sys.exit()
