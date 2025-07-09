import pygame

pygame.init()

muhyun = 1

# 화면 생성
GameDisplay = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("타워 디펜스")

# 이미지 불러오기
background1 = pygame.image.load("./대충 개쩌는 배경.png")
background2 = pygame.image.load("./시작화면.png")
sk_tower = pygame.image.load("./skton_arrow.png")
sk_tower = pygame.transform.scale(sk_tower, (100, 150))
gameExitMes = pygame.image.load("./gameExitMes.png")

#include <stdio.h> sex

# 폰트 설정
font = pygame.font.Font("./DungGeunMo.ttf", 80)

# 텍스트
start = font.render("Press ENTER to start!!", True, (0, 0, 0))
exitMes = font.render("게임을 종료하시겠습니까?", True, (0, 0, 0))
exitMesTrue = font.render("네", True, (0, 0, 0))
exitMesFalse = font.render("아니오", True, (0, 0, 0))

# 버튼 위치 및 Rect
button_pos = (1820, 250)
button_rect = sk_tower.get_rect(topleft=button_pos)

# 상태 변수들
gamepage = 0
running = True
dragging_tower = False
placed_towers = []
esc_mode = False

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 시작 화면에서 엔터키 입력
        if gamepage == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                gamepage = 1

        # 게임 화면에서 클릭 처리
        if gamepage == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    dragging_tower = True  # 버튼 클릭 -> 타워 따라가기 시작
            if event.type == pygame.MOUSEBUTTONUP:
                if dragging_tower:
                    placed_towers.append(event.pos)  # 설치 위치 저장
                    dragging_tower = False

        #ESC키를 누르면 종료
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                esc_mode = not esc_mode
        if esc_mode:
            yesButton = pygame.Rect(533, 659, 321, 128)
            noButton = pygame.Rect(1047, 650, 354, 126)
            #게임 종료처리 or 남기처리
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yesButton.collidepoint(pygame.mouse.get_pos()):
                        running = False
                        esc_mode = False
                    elif noButton.collidepoint(pygame.mouse.get_pos()):
                        esc_mode = False

    # 화면 그리기
    if gamepage == 0:
        GameDisplay.blit(background1, (0, 0))
        GameDisplay.blit(start, (500, 490))

    elif gamepage == 1:
        GameDisplay.blit(background2, (0, 0))

        # 버튼 이미지
        GameDisplay.blit(sk_tower, button_pos)

        # 설치된 타워들
        for pos in placed_towers:
            rect = sk_tower.get_rect(center=pos)
            GameDisplay.blit(sk_tower, rect.topleft)

        # 드래그 중일 때 마우스 따라오기
        if dragging_tower:
            mx, my = pygame.mouse.get_pos()
            rect = sk_tower.get_rect(center=(mx, my))
            GameDisplay.blit(sk_tower, rect.topleft)
        
        if esc_mode:
            GameDisplay.blit(gameExitMes, (360,203))
            GameDisplay.blit(exitMes, (425,350))
            GameDisplay.blit(exitMesTrue, (660, 670))
            GameDisplay.blit(exitMesFalse, (1100, 670))

    # 다른 페이지가 생겨도 타워는 안 보임

    pygame.display.update()

pygame.quit()
