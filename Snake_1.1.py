import pygame
import random
from pygame import mixer
import time
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
bg = pygame.image.load("hlavnaplocha.jpg")
bg2 = pygame.image.load("pozadie_menulevely.jpg")
bg3 = pygame.image.load("Pozadie.jpg")
bg4 = pygame.image.load("pozadie_hry.png")
bg5 = pygame.image.load ("gameover.jpg")
bg6 = pygame.image.load("About.jpg")
bg7 = pygame.image.load("howtoplay.jpg")
bg8 = pygame.image.load("gamepaused.jpg")
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
#FONT
font1 = pygame.font.SysFont("Edo", 35)
font2 = pygame.font.SysFont("Showcard Gothic", 80)
font3 = pygame.font.SysFont("MV Boli", 30)
#LEADERBOARD
list_score1 = [0]
list_score2 = [0]
list_score3 = [0]
list_score4 = [0]
premenna1 = 0
premenna2 = 0
premenna3 = 0
premenna4 = 0
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

def snake_farba():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        text_obrazovky("Vyber farbu hada:", farba_biela, 292, 175)
        text_obrazovky("[1] - zelená", farba_biela, 300, 287)
        text_obrazovky("[2] - biela", farba_biela, 300, 400)
        text_obrazovky("  [3] - tyrkisová", farba_biela, 305, 530)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    menu2()
                global farba_hada
                if event.key == pygame.K_KP1:
                    farba_hada = farba_zelena
                    menu2()
                if event.key == pygame.K_KP2:
                    farba_hada = farba_biela
                    menu2()
                if event.key == pygame.K_KP3:
                    farba_hada = farba_svetlo_modra
                    menu2()
            if event.type == pygame.QUIT:
                zrusit_hru = True
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
            premenna1 = score
            global list_score1
            list_score1[0] = premenna1
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 476, 356)

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
            text_obrazovky( str(score), farba_biela, 48, 11)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 2)

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
            premenna2 = score
            global list_score2
            list_score2[0] = premenna2
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 476, 356)

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
            text_obrazovky( str(score), farba_biela, 48, 11)
            pygame.draw.rect(screen, farba_cervena, [jablko1_x, jablko1_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko2_x, jablko2_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko3_x, jablko3_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko4_x, jablko4_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 2)

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
            premenna3 = score
            global list_score3
            list_score3[0] = premenna3
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 476, 356)

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
            text_obrazovky( str(score), farba_biela, 48, 11)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 2)

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
            premenna4 = score
            global list_score4
            list_score4[0] = premenna4
            screen.blit(bg5, (0, 0))
            text_obrazovky3("" + str(score), farba_cierna, 476, 356)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_levely2()

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

            if abs(snake_x - dead1_x) < 40 and abs(snake_y - dead1_y) < 40:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead2_x) < 40 and abs(snake_y - dead2_y) < 40:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead3_x) < 40 and abs(snake_y - dead3_y) < 40:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead4_x) < 40 and abs(snake_y - dead4_y) < 40:
                efekt2.play()
                koniec_hry = True

            if abs(snake_x - dead5_x) < 40 and abs(snake_y - dead5_y) < 40:
                efekt2.play()
                koniec_hry = True

            screen.blit(bg4, (0, 0))
            text_obrazovky(str(score), farba_biela, 48, 11)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cierna, [dead1_x, dead1_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead2_x, dead2_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead3_x, dead3_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead4_x, dead4_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.rect(screen, farba_cierna, [dead5_x, dead5_y, velkost_hada + 30, velkost_hada + 30])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 2)

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
    pygame.quit()
    quit()

#Menu
def menu():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        text_obrazovky("PLAY", farba_biela, 370, 175)
        text_obrazovky("LEADERBOARD", farba_biela, 305, 287)
        text_obrazovky("OPTIONS", farba_biela, 340, 400)
        text_obrazovky(" EXIT", farba_biela, 362, 530)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    zrusit_hru = True
                    quit()
                if event.key == pygame.K_KP1:
                    menu_levely()
                if event.key == pygame.K_KP2:
                    leaderboard()
                if event.key == pygame.K_KP3:
                    menu2()
            if event.type == pygame.QUIT:
                zrusit_hru = True
                pygame.quit()
                quit()

def menu_levely():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg2, (0, 0))
        text_obrazovky("CLASSIC", farba_biela, 344, 173)
        text_obrazovky("MULTI APPLE", farba_biela, 317, 287)
        text_obrazovky("NEXT", farba_biela, 370, 400)
        text_obrazovky("BACK", farba_biela, 364, 530)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    game()
                if event.key == pygame.K_KP2:
                    game2()
                if event.key == pygame.K_KP3:
                    menu_levely2()
                if event.key == pygame.K_KP4:
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()

def menu_levely2():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg2, (0, 0))
        text_obrazovky("FASTER BIGGER", farba_biela, 305, 173)
        text_obrazovky("DEAD BLOCKS", farba_biela, 310, 287)
        text_obrazovky("BACK", farba_biela, 364, 400)
        text_obrazovky("MENU", farba_biela, 364, 530)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    game3()
                if event.key == pygame.K_KP2:
                    game4()
                if event.key == pygame.K_KP3:
                    menu_levely()
                if event.key == pygame.K_KP4:
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()

def about():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg6, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    menu()
                if event.key == pygame.K_KP2:
                    howtoplay()
            if event.type == pygame.QUIT:
                pygame.quit()

def howtoplay():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg7, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    about()
            if event.type == pygame.QUIT:
                pygame.quit()

def leaderboard():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        global list_score1
        global list_score2
        global list_score3
        text_obrazovky("Classic: " + str(list_score1), farba_biela, 300, 175)
        text_obrazovky("Multi apple: " + str(list_score2), farba_biela, 300, 287)
        text_obrazovky(" NEXT", farba_biela, 362, 400)
        text_obrazovky(" BACK", farba_biela, 362, 530)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP3:
                    leaderboard2()
                if event.key == pygame.K_KP4:
                    menu()
            if event.type == pygame.QUIT:
                zrusit_hru = True
                pygame.quit()
                quit()

def leaderboard2():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        global list_score3
        global list_score4
        text_obrazovky("FASTER BIGGER:" + str(list_score3), farba_biela, 300, 175)
        text_obrazovky("DEAD BLOCKS:" + str(list_score4), farba_biela, 300, 287)
        text_obrazovky(" BACK", farba_biela, 362, 400)
        text_obrazovky(" MENU", farba_biela, 362, 530)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP3:
                    leaderboard()
                if event.key == pygame.K_KP4:
                    menu()
            if event.type == pygame.QUIT:
                zrusit_hru = True
                pygame.quit()
                quit()

def menu2():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        text_obrazovky("FARBA HADA", farba_biela, 320, 175)
        text_obrazovky("        ABOUT", farba_biela, 305, 287)
        text_obrazovky(" BACK", farba_biela, 360, 400)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP3:
                    menu()
                if event.key == pygame.K_KP1:
                    snake_farba()
                if event.key == pygame.K_KP2:
                    about()
            if event.type == pygame.QUIT:
                zrusit_hru = True
                pygame.quit()
                quit()

menu()
