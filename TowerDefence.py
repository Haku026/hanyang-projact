import pygame

pygame.init()

muhyun = 1
# 화면 생성
GameDisplay = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("타워 디펜스")

# 이미지 불러오기
background1 = pygame.image.load("./대충 개쩌는 배경.png")
background2 = pygame.image.load("./시작화면.png")
gameExitMes = pygame.image.load("./게임종료화면.png")
easyMapUI = pygame.image.load("./쉬움맵.png")
normalMapUI = pygame.image.load("./보통맵.png")
hardMapUI = pygame.image.load("./어려움맵.png")
mainMenuUI = pygame.image.load("./메인메뉴 UI.png")


# 폰트 설정
font = pygame.font.Font("./DungGeunMo.ttf", 80)

# 텍스트
start = font.render("Press ENTER to start!!", True, (0, 0, 0))
exitMes = font.render("게임을 종료하시겠습니까?", True, (0, 0, 0))
exitMesTrue = font.render("네", True, (0, 0, 0))
exitMesFalse = font.render("아니오", True, (0, 0, 0))


# 상태 변수들
gamepage = 0
running = True
esc_mode = False

        


# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 클릭 위치 출력
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        # 시작 화면에서 엔터키 입력
        if gamepage == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                gamepage = 1


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
        GameDisplay.blit(mainMenuUI, (150,780))


    if esc_mode:
            GameDisplay.blit(gameExitMes, (360,203))
            GameDisplay.blit(exitMes, (425,350))
            GameDisplay.blit(exitMesTrue, (660, 670))
            GameDisplay.blit(exitMesFalse, (1100, 670))    

    pygame.display.update()

pygame.quit()
