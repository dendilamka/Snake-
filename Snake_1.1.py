import pygame
import random
from pygame import mixer
import time
text = ""
#intialize the pygame
pygame.init()
#Spustenie hudby
mixer.init()
#HUDBA
mixer.music.load("bg_music.mp3")
efekt = mixer.Sound("food.mp3")
efekt2 = mixer.Sound("fail.mp3")
efekt.set_volume(0.2)
efekt2.set_volume(0.1)
mixer.music.set_volume(0.02)
mixer.music.play()
#ROZLÍŠENIE
res = (800, 600)
#OTVORIŤ OKNO
screen = pygame.display.set_mode(res)
#ŠÍRKA A VÝŠKA
sirka = screen.get_width()
vyska = screen.get_height()
#POZADIE
bg = pygame.image.load("Pozadie_menu.jpg")
bg2 = pygame.image.load("Pozadie_levels.jpg")
bg3 = pygame.image.load("Pozadie.jpg")
bg4 = pygame.image.load("pozadie_game.jpg")
bg5 = pygame.image.load ("Pozadie_gameover.jpg")
bg6 = pygame.image.load("Pozadie_about.jpg")
bg7 = pygame.image.load("Pozadie_howtoplay.jpg")
bg8 = pygame.image.load("gamepaused.jpg")
bg9 = pygame.image.load("Pozadie_settings.jpg")
bg10 = pygame.image.load("Pozadie_musicsettings.jpg")
bg11 = pygame.image.load("Pozadie_changecolor.jpg")
bg12 = pygame.image.load("Pozadie_login.jpg")
bg13 = pygame.image.load("pozadie_leaderboar.jpg")
#NÁZOV a Icona
pygame.display.set_caption("Hungry Snake")
icon = pygame.image.load("Snake-icon.png")
pygame.display.set_icon(icon)
pygame.display.update()
#HODINY
clock = pygame.time.Clock()
#FARBY
farba_siva_tmava = (100, 100, 100)
farba_biela = (255, 255, 255)
farba_zelena = (0, 128, 0)
farba_cervena = (255, 0, 0)
farba_cierna = (0, 0, 0)
farba_svetlo_modra = (0, 255, 255)
farba_hada = (0, 128, 0)
farba_siva = (165, 165, 165)
farba_zlta = (255, 255, 0)
#FONT
font1 = pygame.font.SysFont("Edo", 35)
font2 = pygame.font.SysFont("Showcard Gothic", 80)
font3 = pygame.font.SysFont("MV Boli", 30)
#LEADERBOARD
list_score1 = 0
list_score2 = 0
list_score3 = 0
list_score4 = 0
list_score5 = 0
premenna1 = 0
premenna2 = 0
premenna3 = 0
premenna4 = 0
premenna5 = 0
#TEXTY
def text_obrazovky(text, farba, x, y):
    text_obrazovky = font1.render(text, True, farba)
    screen.blit(text_obrazovky, [x,y])

def text_obrazovky2(text, farba, x, y):
    text_obrazovky2 = font2.render(text, True, farba)
    screen.blit(text_obrazovky2, [x,y])

def text_obrazovky3(text, farba, x, y):
    text_obrazovky3 = font3.render(text, True, farba)
    screen.blit(text_obrazovky3, [x,y])

#PAUSE
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_e:
                    pygame.quit()
                    quit()

        screen.blit(bg8, (0, 0))
        pygame.display.update()
        clock.tick(10)

#HAD
def snake(screen, farba, list, velkost_hada):
    for x,y in list:
        pygame.draw.rect(screen, farba, [x,y, velkost_hada, velkost_hada])

def snake2(screen, farba, list2, velkost_hada2):
    for x,y in list2:
        pygame.draw.rect(screen, farba, [x,y, velkost_hada2, velkost_hada2])

def snake_farba():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg11, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 308 and mx <= 490 and my >= 529 and my <= 576:
                    menu2()
                if mx >= 287 and mx <= 513 and my >= 146 and my <= 193:
                    farba_hada = farba_zelena
                    menu2()
                if mx >= 287 and mx <= 513 and my >= 223 and my <= 270:
                    farba_hada = farba_biela
                    menu2()
                if mx >= 287 and mx <= 513 and my >= 306 and my <= 354:
                    farba_hada = farba_svetlo_modra
                    menu2()
                if mx >= 287 and mx <= 513 and my >= 383 and my <= 431:
                    farba_hada = farba_zlta
                    menu2()
            if event.type == pygame.QUIT:
                zrusit_hru = True
                uloz_skore()
                pygame.quit()
                quit()

#HRA
def game():
    posledný_pohyb = "ziadny"
    zrusit_hru = False
    koniec_hry = False
    snake_x = 400
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    list = []
    dlzka = 1
    jablko_x = random.randint(20, sirka - 20)
    jablko_y = random.randint(60, vyska - 20)
    score = 0
    init_velocity = 4
    velkost_hada = 30
    fps = 60
    while not zrusit_hru:
        if koniec_hry:
            global premenna1
            global list_score1
            premenna1 = score
            if (list_score1 < premenna1):
                list_score1 = premenna1
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 471, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_levely()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        if (posledný_pohyb != "do lava"):
                            velocity_x = init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do prava"

                    if event.key == pygame.K_LEFT:
                        if (posledný_pohyb != "do prava"):
                            velocity_x = - init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do lava"

                    if event.key == pygame.K_UP:
                        if (posledný_pohyb != "dole"):
                            velocity_y = - init_velocity
                            velocity_x = 0
                            posledný_pohyb = "hore"

                    if event.key == pygame.K_DOWN:
                        if (posledný_pohyb != "hore"):
                            velocity_y = init_velocity
                            velocity_x = 0
                            posledný_pohyb = "dole"

                    elif event.key == pygame.K_ESCAPE:
                        pause()


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - jablko_x) < 20 and abs(snake_y - jablko_y) < 20:
                efekt.play()
                score += 1
                jablko_x = random.randint(20, sirka - 30)
                jablko_y = random.randint(60, vyska - 30)
                dlzka += 5

            screen.blit(bg4, (0, 0))
            text_obrazovky( str(score), farba_siva, 85, 9)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_siva, (0, 40), (800, 40), 4)

            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                efekt2.play()
                koniec_hry = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                efekt2.play()
                koniec_hry = True
            snake(screen, farba_hada, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    uloz_skore()
    pygame.quit()
    quit()

def game2():
    posledný_pohyb = "ziadny"
    zrusit_hru = False
    koniec_hry = False
    snake_x = 400
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    list = []
    dlzka = 1
    jablko1_x = random.randint(20, sirka - 20)
    jablko1_y = random.randint(60, vyska - 20)
    jablko2_x = random.randint(20, sirka - 20)
    jablko2_y = random.randint(60, vyska - 20)
    jablko3_x = random.randint(20, sirka - 20)
    jablko3_y = random.randint(60, vyska - 20)
    jablko4_x = random.randint(20, sirka - 20)
    jablko4_y = random.randint(60, vyska - 20)
    score = 0
    init_velocity = 4
    velkost_hada = 30
    fps = 60
    while not zrusit_hru:
        if koniec_hry:
            global premenna2
            global list_score2
            premenna2 = score
            if (list_score2 < premenna2):
                list_score2 = premenna2
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 471, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_levely()


        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:

                        if (posledný_pohyb != "do lava"):
                            velocity_x = init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do prava"

                    if event.key == pygame.K_LEFT:

                        if (posledný_pohyb != "do prava"):
                            velocity_x = - init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do lava"

                    if event.key == pygame.K_UP:

                        if (posledný_pohyb != "dole"):
                            velocity_y = - init_velocity
                            velocity_x = 0
                            posledný_pohyb = "hore"

                    if event.key == pygame.K_DOWN:

                        if (posledný_pohyb != "hore"):
                            velocity_y = init_velocity
                            velocity_x = 0
                            posledný_pohyb = "dole"

                    elif event.key == pygame.K_ESCAPE:
                        pause()


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - jablko1_x) < 20 and abs(snake_y - jablko1_y) < 20:
                efekt.play()
                score += 1
                jablko1_x = random.randint(20, sirka - 30)
                jablko1_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - jablko2_x) < 20 and abs(snake_y - jablko2_y) < 20:
                efekt.play()
                score += 1
                jablko2_x = random.randint(20, sirka - 30)
                jablko2_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - jablko3_x) < 20 and abs(snake_y - jablko3_y) < 20:
                efekt.play()
                score += 1
                jablko3_x = random.randint(20, sirka - 30)
                jablko3_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - jablko4_x) < 20 and abs(snake_y - jablko4_y) < 20:
                efekt.play()
                score += 1
                jablko4_x = random.randint(20, sirka - 30)
                jablko4_y = random.randint(60, vyska - 30)
                dlzka += 5


            screen.blit(bg4, (0, 0))
            text_obrazovky(str(score), farba_siva, 85, 9)
            pygame.draw.rect(screen, farba_cervena, [jablko1_x, jablko1_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko2_x, jablko2_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko3_x, jablko3_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko4_x, jablko4_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_siva, (0, 40), (800, 40), 4)

            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                efekt2.play()
                koniec_hry = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                efekt2.play()
                koniec_hry = True
            snake(screen, farba_hada, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    uloz_skore()
    pygame.quit()
    quit()

def game3():
    posledný_pohyb = "ziadny"
    zrusit_hru = False
    koniec_hry = False
    snake_x = 400
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    list = []
    dlzka = 1
    jablko_x = random.randint(20, sirka - 20)
    jablko_y = random.randint(60, vyska - 20)
    score = 0
    init_velocity = 6
    velkost_hada = 30
    fps = 60
    while not zrusit_hru:
        if koniec_hry:
            global premenna3
            global list_score3
            premenna3 = score
            if (list_score3 < premenna3):
                list_score3 = premenna3
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 471, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_levely()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        if (posledný_pohyb != "do lava"):
                            velocity_x = init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do prava"

                    if event.key == pygame.K_LEFT:
                        if (posledný_pohyb != "do prava"):
                            velocity_x = - init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do lava"

                    if event.key == pygame.K_UP:
                        if (posledný_pohyb != "dole"):
                            velocity_y = - init_velocity
                            velocity_x = 0
                            posledný_pohyb = "hore"

                    if event.key == pygame.K_DOWN:
                        if (posledný_pohyb != "hore"):
                            velocity_y = init_velocity
                            velocity_x = 0
                            posledný_pohyb = "dole"

                    elif event.key == pygame.K_ESCAPE:
                        pause()


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - jablko_x) < 20 and abs(snake_y - jablko_y) < 20:
                efekt.play()
                score += 1
                if ((score == 10) or (score == 20) or (score == 30) or (score == 40)):
                    init_velocity = init_velocity + 1
                jablko_x = random.randint(20, sirka - 30)
                jablko_y = random.randint(60, vyska - 30)
                dlzka += 10

            screen.blit(bg4, (0, 0))
            text_obrazovky(str(score), farba_siva, 85, 9)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_siva, (0, 40), (800, 40), 4)

            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                efekt2.play()
                koniec_hry = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                efekt2.play()
                koniec_hry = True
            snake(screen, farba_hada, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    uloz_skore()
    pygame.quit()
    quit()

def game4():
    posledný_pohyb = "ziadny"
    zrusit_hru = False
    koniec_hry = False
    snake_x = 400
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    list = []
    dlzka = 1
    dead5_x = random.randint(20, sirka - 20)
    dead5_y = random.randint(60, vyska - 20)
    dead4_x = random.randint(20, sirka - 20)
    dead4_y = random.randint(60, vyska - 20)
    dead3_x = random.randint(20, sirka - 20)
    dead3_y = random.randint(60, vyska - 20)
    dead2_x = random.randint(20, sirka - 20)
    dead2_y = random.randint(60, vyska - 20)
    dead1_x = random.randint(20, sirka - 20)
    dead1_y = random.randint(60, vyska - 20)
    jablko_x = random.randint(20, sirka - 20)
    jablko_y = random.randint(60, vyska - 20)
    score = 0
    init_velocity = 4
    velkost_hada = 30
    fps = 60
    while not zrusit_hru:
        if koniec_hry:
            global premenna4
            global list_score4
            premenna4 = score
            if(list_score4 < premenna4):
                list_score4 = premenna4
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 471, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_levely()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        if (posledný_pohyb != "do lava"):
                            velocity_x = init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do prava"

                    if event.key == pygame.K_LEFT:
                        if (posledný_pohyb != "do prava"):
                            velocity_x = - init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do lava"

                    if event.key == pygame.K_UP:
                        if (posledný_pohyb != "dole"):
                            velocity_y = - init_velocity
                            velocity_x = 0
                            posledný_pohyb = "hore"

                    if event.key == pygame.K_DOWN:
                        if (posledný_pohyb != "hore"):
                            velocity_y = init_velocity
                            velocity_x = 0
                            posledný_pohyb = "dole"

                    elif event.key == pygame.K_ESCAPE:
                        pause()

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - jablko_x) < 20 and abs(snake_y - jablko_y) < 20:
                efekt.play()
                score += 1
                jablko_x = random.randint(20, sirka - 30)
                jablko_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - dead1_x) < 35 and abs(snake_y - dead1_y) < 35:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead2_x) < 35 and abs(snake_y - dead2_y) < 35:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead3_x) < 35 and abs(snake_y - dead3_y) < 35:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead4_x) < 35 and abs(snake_y - dead4_y) < 35:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead5_x) < 35 and abs(snake_y - dead5_y) < 35:
                efekt2.play()
                koniec_hry = True

            screen.blit(bg4, (0, 0))
            text_obrazovky(str(score), farba_siva, 85, 9)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cierna, [dead1_x, dead1_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead2_x, dead2_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead3_x, dead3_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead4_x, dead4_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead5_x, dead5_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.line(screen, farba_siva, (0, 40), (800, 40), 4)

            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                efekt2.play()
                koniec_hry = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                efekt2.play()
                koniec_hry = True
            snake(screen, farba_hada, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    uloz_skore()
    pygame.quit()
    quit()

def game5():
    posledný_pohyb = "ziadny"
    posledný_pohyb2 = "ziadny"
    zrusit_hru = False
    koniec_hry = False
    snake_x = 400
    snake_y = 250
    snake2_x = 400
    snake2_y = 350
    velocity_x = 0
    velocity_y = 0
    velocity2_x = 0
    velocity2_y = 0
    list = []
    list2 = []
    dlzka = 1
    dlzka2 = 1
    jablko1_x = random.randint(20, sirka - 20)
    jablko1_y = random.randint(60, vyska - 20)
    jablko2_x = random.randint(20, sirka - 20)
    jablko2_y = random.randint(60, vyska - 20)
    jablko3_x = random.randint(20, sirka - 20)
    jablko3_y = random.randint(60, vyska - 20)
    jablko4_x = random.randint(20, sirka - 20)
    jablko4_y = random.randint(60, vyska - 20)
    score = 0
    init_velocity = 4
    velkost_hada = 30
    init_velocity2 = 4
    velkost_hada2 = 30
    fps = 60
    while not zrusit_hru:
        if koniec_hry:
            global premenna5
            global list_score5
            premenna5 = score
            if (list_score5 < premenna5):
                list_score5 = premenna5
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 471, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_levely()


        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:

                        if (posledný_pohyb != "do lava"):
                            velocity_x = init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do prava"

                    if event.key == pygame.K_LEFT:

                        if (posledný_pohyb != "do prava"):
                            velocity_x = - init_velocity
                            velocity_y = 0
                            posledný_pohyb = "do lava"

                    if event.key == pygame.K_UP:

                        if (posledný_pohyb != "dole"):
                            velocity_y = - init_velocity
                            velocity_x = 0
                            posledný_pohyb = "hore"

                    if event.key == pygame.K_DOWN:

                        if (posledný_pohyb != "hore"):
                            velocity_y = init_velocity
                            velocity_x = 0
                            posledný_pohyb = "dole"

                    if event.key == pygame.K_d:

                        if (posledný_pohyb2 != "do lava"):
                            velocity2_x = init_velocity2
                            velocity2_y = 0
                            posledný_pohyb2 = "do prava"

                    if event.key == pygame.K_a:

                        if (posledný_pohyb2 != "do prava"):
                            velocity2_x = - init_velocity2
                            velocity2_y = 0
                            posledný_pohyb2 = "do lava"

                    if event.key == pygame.K_w:

                        if (posledný_pohyb2 != "dole"):
                            velocity2_y = - init_velocity2
                            velocity2_x = 0
                            posledný_pohyb2 = "hore"

                    if event.key == pygame.K_s:

                        if (posledný_pohyb2 != "hore"):
                            velocity2_y = init_velocity2
                            velocity2_x = 0
                            posledný_pohyb2 = "dole"

                    elif event.key == pygame.K_ESCAPE:
                        pause()

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            snake2_x = snake2_x + velocity2_x
            snake2_y = snake2_y + velocity2_y

            if abs(snake_x - jablko1_x) < 20 and abs(snake_y - jablko1_y) < 20:
                efekt.play()
                score += 1
                jablko1_x = random.randint(20, sirka - 30)
                jablko1_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - jablko2_x) < 20 and abs(snake_y - jablko2_y) < 20:
                efekt.play()
                score += 1
                jablko2_x = random.randint(20, sirka - 30)
                jablko2_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - jablko3_x) < 20 and abs(snake_y - jablko3_y) < 20:
                efekt.play()
                score += 1
                jablko3_x = random.randint(20, sirka - 30)
                jablko3_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake_x - jablko4_x) < 20 and abs(snake_y - jablko4_y) < 20:
                efekt.play()
                score += 1
                jablko4_x = random.randint(20, sirka - 30)
                jablko4_y = random.randint(60, vyska - 30)
                dlzka += 5

            if abs(snake2_x - jablko1_x) < 20 and abs(snake2_y - jablko1_y) < 20:
                efekt.play()
                score += 1
                jablko1_x = random.randint(20, sirka - 30)
                jablko1_y = random.randint(60, vyska - 30)
                dlzka2 += 5

            if abs(snake2_x - jablko2_x) < 20 and abs(snake2_y - jablko2_y) < 20:
                efekt.play()
                score += 1
                jablko2_x = random.randint(20, sirka - 30)
                jablko2_y = random.randint(60, vyska - 30)
                dlzka2 += 5

            if abs(snake2_x - jablko3_x) < 20 and abs(snake2_y - jablko3_y) < 20:
                efekt.play()
                score += 1
                jablko3_x = random.randint(20, sirka - 30)
                jablko3_y = random.randint(60, vyska - 30)
                dlzka2 += 5

            if abs(snake2_x - jablko4_x) < 20 and abs(snake2_y - jablko4_y) < 20:
                efekt.play()
                score += 1
                jablko4_x = random.randint(20, sirka - 30)
                jablko4_y = random.randint(60, vyska - 30)
                dlzka2 += 5

            screen.blit(bg4, (0, 0))
            text_obrazovky(str(score), farba_siva, 85, 9)
            pygame.draw.rect(screen, farba_cervena, [jablko1_x, jablko1_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko2_x, jablko2_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko3_x, jablko3_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko4_x, jablko4_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_siva, (0, 40), (800, 40), 4)

            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                efekt2.play()
                koniec_hry = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                efekt2.play()
                koniec_hry = True
            snake(screen, farba_hada, list, velkost_hada)

            hlava2 = []
            hlava2.append(snake2_x)
            hlava2.append(snake2_y)
            list2.append(hlava2)

            if len(list2) > dlzka2:
                del list2[0]

            if hlava2 in list2[:-1]:
                efekt2.play()
                koniec_hry = True

            if snake2_x < 0 or snake2_x > sirka - 20 or snake2_y < 50 or snake2_y > vyska - 20:
                efekt2.play()
                koniec_hry = True
            snake2(screen, farba_zlta, list2, velkost_hada2)

        pygame.display.update()
        clock.tick(fps)
    uloz_skore()
    pygame.quit()
    quit()

#Menu
def menu():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 273 and mx <= 525 and my >= 200 and my <= 230:
                    menu_levely()
                if mx >= 273 and mx <= 525 and my >= 274 and my <= 325:
                    leaderboard()
                if mx >= 273 and mx <= 525 and my >= 369 and my <= 422:
                    menu2()
                if mx >= 273 and mx <= 525 and my >= 513 and my <= 572:
                    quit()
            if event.type == pygame.QUIT:
                uloz_skore()
                zrusit_hru = True
                pygame.quit()
                quit()

def menu_levely():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg2, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 287 and mx <= 513 and my >= 145 and my <= 192:
                    game()
                if mx >= 287 and mx <= 513 and my >= 226 and my <= 274:
                    game2()
                if mx >= 287 and mx <= 513 and my >= 309 and my <= 356:
                    game3()
                if mx >= 287 and mx <= 513 and my >= 392 and my <= 439:
                    game4()
                if mx >= 287 and mx <= 513 and my >= 529 and my <= 577:
                    menu()
            if event.type == pygame.QUIT:
                uloz_skore()
                pygame.quit()

def about():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg6, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 52 and mx <= 234 and my >= 528 and my <= 576:
                    menu()
                if mx >= 565 and mx <= 748 and my >= 529 and my <= 576:
                    howtoplay()
            if event.type == pygame.QUIT:
                uloz_skore()
                pygame.quit()

def howtoplay():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg7, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 308 and mx <= 491 and my >= 529 and my <= 576:
                    about()
            if event.type == pygame.QUIT:
                uloz_skore()
                pygame.quit()

def leaderboard():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg13, (0, 0))
        global list_score1
        global list_score2
        global list_score3
        global list_score4
        global list_score5
        text_obrazovky("" + str(list_score1), farba_cervena, 506, 239)
        text_obrazovky("" + str(list_score2), farba_cervena, 506, 283)
        text_obrazovky("" + str(list_score3), farba_cervena, 506, 334)
        text_obrazovky("" + str(list_score4), farba_cervena, 506, 386)
        text_obrazovky("" + str(list_score5), farba_cervena, 506, 437)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 309 and mx <= 491 and my >= 528 and my <= 576:
                    menu()
            if event.type == pygame.QUIT:
                uloz_skore()
                zrusit_hru = True
                pygame.quit()
                quit()

def musicsettings():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg10, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 286 and mx <= 514 and my >= 173 and my <= 220 :
                    mixer.music.play()
                    efekt.set_volume(0.2)
                    efekt2.set_volume(0.1)
                if mx >= 286 and mx <= 514 and my >= 265 and my <= 313:
                    mixer.music.stop()
                    efekt.set_volume(0.0)
                    efekt2.set_volume(0.0)
                if mx >= 306 and mx <= 492  and my >= 529 and my <= 576:
                    menu2()
            if event.type == pygame.QUIT:
                uloz_skore()
                zrusit_hru = True
                pygame.quit()
                quit()

def menu2():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg9, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 306 and mx <= 492  and my >= 529 and my <= 576:
                    menu()
                if mx >= 286 and mx <= 514  and my >= 173 and my <= 220:
                    snake_farba()
                if mx >= 286 and mx <= 514 and my >= 265 and my <= 313:
                    musicsettings()
                if mx >= 286 and mx <= 514 and my >= 357 and my <= 406:
                    about()
            if event.type == pygame.QUIT:
                uloz_skore()
                zrusit_hru = True
                pygame.quit()
                quit()

def login():
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("Showcard Gothic", 60)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(230, 300, 140, 60)
    zrusit_hru = False
    active = False
    global Meno
    Meno = ''
    global text
    text = ''
    color_inactive = farba_siva
    color_active = farba_hada
    color = color_inactive
    while not zrusit_hru:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                uloz_skore()
                zrusit_hru = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                if input_box.collidepoint(event.pos):

                    active = not active
                else:
                    active = False

                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        a = open("Meno.txt", "a+")
                        Meno = text
                        a.write(f"{Meno} \n")
                        a.close()
                        text = ''
                        menu()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.blit(bg12, (0, 0))
        pygame.display.update()
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(340, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

def uloz_skore():
    a = open("Meno.txt", "a+")
    a.write(f"Classic: {list_score1} \n")
    a.write(f"Multi Apple: {list_score2} \n")
    a.write(f"Faster Bigger: {list_score3} \n")
    a.write(f"Dead Blocks: {list_score4} \n")
    a.write(f"2 PLAYES: {list_score5} \n")
    a.close()

login()
