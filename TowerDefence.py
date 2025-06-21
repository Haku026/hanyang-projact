import pygame

pygame.init()

muhyun = 1

# 화면 생성
GameDisplay = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("타워 디펜스")

# 이미지 불러오기
background1 = pygame.image.load("C:/Users/B760I/Desktop/hanyang-projact/대충 개쩌는 배경.png")
background2 = pygame.image.load("C:/Users/B760I/Desktop/hanyang-projact/대충 개쩌는 메인화면.png")
sk_tower = pygame.image.load("C:/Users/B760I/Desktop/hanyang-projact/skton_arrow.png")
sk_tower = pygame.transform.scale(sk_tower, (100, 150))

# 폰트 설정
font = pygame.font.Font("C:/Users/B760I/Desktop/hanyang-projact/DungGeunMo.ttf", 100)

# 텍스트
start = font.render("Press ENTER to start!!", True, (0, 0, 0))

# 버튼 위치 및 Rect
button_pos = (1820, 250)
button_rect = sk_tower.get_rect(topleft=button_pos)

# 상태 변수들
gamepage = 0
running = True
dragging_tower = False
placed_towers = []

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

    # 다른 페이지가 생겨도 타워는 안 보임

    pygame.display.update()

pygame.quit()
