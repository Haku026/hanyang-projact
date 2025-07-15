import pygame
import os
time = pygame.time.Clock()

pygame.init()

muhyun = 1
# 화면 생성
GameDisplay = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("타워 디펜스")

# 배경 불러오기
background1 = pygame.image.load("./맵/대충 개쩌는 배경.png")
background2 = pygame.image.load("./맵/시작화면.png")
gameExitMes = pygame.image.load("./맵/게임종료화면.png")
easyMapUI = pygame.image.load("./맵/쉬움맵.png")
normalMapUI = pygame.image.load("./맵/보통맵.png")
hardMapUI = pygame.image.load("./맵/어려움맵.png")
mainMenuUI = pygame.image.load("./맵/기모찌.png")

# 캐릭터 불러오기
skeleton_tower = [pygame.transform.scale(pygame.image.load(f"./타워/스켈타워/서서움직임/스켈레톤 타워{i}.png"),(128, 128)) #크기조절
    for i in range(1, 7)]
goblin_tower = [pygame.transform.scale(pygame.image.load(f"./타워/고블린타워/서서움직임/고블린 타워{i}.png"),(128, 128)) #크기조절
    for i in range(1, 7)]  
image_index = 0

# 음악 불러오기
mainMenuMusic = pygame.mixer.Sound("./배경음악/배경음악.mp3")
mainMenuMusic.set_volume(0.4)  # 볼륨 설정 (0.0 ~ 1.0)

enterSoundEffect = pygame.mixer.Sound("./배경음악/시작 효과음.wav")
enterSoundEffect.set_volume(1.0)

mapSelectBGM = pygame.mixer.Sound("./배경음악/맵선택bgm.mp3")
mapSelectBGM.set_volume(0.4)

# 폰트 설정
font = pygame.font.Font("./폰트/DungGeunMo.ttf", 80)

# 텍스트
start = font.render("Press ENTER to start!!", True, (0, 0, 0))
exitMes = font.render("게임을 종료하시겠습니까?", True, (0, 0, 0))
exitMesTrue = font.render("네", True, (0, 0, 0))
exitMesFalse = font.render("아니오", True, (0, 0, 0))

# 상태 변수들
gamepage = 0
frame_delay = 100 # 몇프레임에 한번 이미지를 바꿀지 설정
frame_timer = 0 # 프레임 카운트 변수
frame_index = 0 # 현재 몇 번 사진으로 할 지 선택
running = True
esc_mode = False
    
# 음악 관련 상태 변수들
isMainMusicOn = True
isMainMusicEffectOn = False
isMapSelectMusicOn = False

# 게임 루프
while running:
    dt = time.tick(60) # 프레임 설정

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 클릭 위치 출력(어디에 놓을지 편의성을 위해)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        # 시작 화면에서 엔터키 입력
        if gamepage == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                isMainMusicEffectOn = True
                mainMenuMusic.stop()
                isMapSelectMusicOn = True
                gamepage = 1
                
        # 음악 발생 처리
        if isMainMusicEffectOn == True:
            enterSoundEffect.play()
            isMainMusicEffectOn = False

        if isMainMusicOn == True:
            mainMenuMusic.play(-1)
            isMainMusicOn = False

        if isMapSelectMusicOn == True:
            mapSelectBGM.play(-1)
            isMapSelectMusicOn = False


        # ESC키를 누르면 종료
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                esc_mode = not esc_mode
        # 게임 종료처리 or 남기처리
        if esc_mode:
            yesButton = pygame.Rect(533, 659, 321, 128)
            noButton = pygame.Rect(1047, 650, 354, 126)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yesButton.collidepoint(pygame.mouse.get_pos()):
                        running = False
                        esc_mode = False
                    elif noButton.collidepoint(pygame.mouse.get_pos()):
                        esc_mode = False
        
    # 타이머 누적
    frame_timer += dt
    if frame_timer >= frame_delay:
        frame_timer = 0
        frame_index = (frame_index + 1) % 6

    # 화면 그리기
    # 메인화면
    if gamepage == 0:
        GameDisplay.blit(background1, (0, 0))
        GameDisplay.blit(start, (500, 490))
    # 메인화면
    elif gamepage == 1:
        GameDisplay.blit(background2, (0, 0))
        GameDisplay.blit(mainMenuUI, (150,780))
    # 타워 그리기
        GameDisplay.blit(skeleton_tower[frame_index], (500, 500))
        GameDisplay.blit(goblin_tower[frame_index], (800, 500))
    


    if esc_mode:
            GameDisplay.blit(gameExitMes, (360,203))
            GameDisplay.blit(exitMes, (425,350))
            GameDisplay.blit(exitMesTrue, (660, 670))
            GameDisplay.blit(exitMesFalse, (1100, 670))    

    pygame.display.update()

pygame.quit()
