import pygame

def In(screen, color, fade_in_speed, alpha_value):    
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background.fill(color)

    # 알파값을 서서히 증가시켜 페이드 인 효과 적용
    for x in range(alpha_value, 60, fade_in_speed):        
        # 배경 이미지 또는 표면에 알파값 적용
        background.set_alpha(x)        
        # 화면에 배경 이미지 그리기
        screen.blit(background, (0, 0))
        pygame.time.delay(10)
        pygame.display.flip()
        
    return True
