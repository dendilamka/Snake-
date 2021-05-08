import pygame
import random
from pygame import mixer
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
bg = pygame.image.load("pozadie_menu.jpg")
bg2 = pygame.image.load("pozadie_menulevely.jpg")
bg3 = pygame.image.load("Pozadie.jpg")
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
#FONT
font1 = pygame.font.SysFont("Edo", 35)
font2 = pygame.font.SysFont("Showcard Gothic", 80)
font3 = pygame.font.SysFont("MV Boli", 30)
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
    screen.blit(bg3, (0, 0))
    text_obrazovky2("PAUSE", farba_cierna, 180, 250)

#HAD
def snake(screen, farba, list, velkost_hada):
    for x,y in list:
        pygame.draw.rect(screen, farba, [x,y, velkost_hada, velkost_hada])

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
            screen.blit(bg3, (0, 0))
            text_obrazovky3("YOUR SCORE: " + str(score), farba_cierna, 280, 350)
            text_obrazovky2("GAME OVER", farba_cierna, 180, 250)

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

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - jablko_x) < 20 and abs(snake_y - jablko_y) < 20:
                efekt.play()
                score += 1
                jablko_x = random.randint(20, sirka - 30)
                jablko_y = random.randint(60, vyska - 30)
                dlzka += 5

            screen.blit(bg3, (0, 0))
            text_obrazovky("Score: " + str(score), farba_biela, 10, 8)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 5)

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
            snake(screen, farba_zelena, list, velkost_hada)
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
            screen.blit(bg3, (0, 0))
            text_obrazovky3("YOUR SCORE: " + str(score), farba_cierna, 280, 350)
            text_obrazovky2("  GAME OVER", farba_cierna, 155, 250)

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


            screen.blit(bg3, (0, 0))
            text_obrazovky("Score: " + str(score), farba_biela, 10, 8)
            pygame.draw.rect(screen, farba_cervena, [jablko1_x, jablko1_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko2_x, jablko2_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko3_x, jablko3_y, velkost_hada, velkost_hada])
            pygame.draw.rect(screen, farba_cervena, [jablko4_x, jablko4_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 5)

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
            snake(screen, farba_zelena, list, velkost_hada)
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
    init_velocity = 4
    velkost_hada = 30
    fps = 60
    while not zrusit_hru:
        if koniec_hry:
            screen.blit(bg3, (0, 0))
            text_obrazovky3("YOUR SCORE: " + str(score), farba_cierna, 280, 350)
            text_obrazovky2("GAME OVER", farba_cierna, 180, 250)

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

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - jablko_x) < 20 and abs(snake_y - jablko_y) < 20:
                efekt.play()
                score += 1
                jablko_x = random.randint(20, sirka - 30)
                jablko_y = random.randint(60, vyska - 30)
                dlzka += 5

            screen.blit(bg3, (0, 0))
            text_obrazovky("Score: " + str(score), farba_biela, 10, 8)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_biela, (0, 40), (800, 40), 5)

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
            snake(screen, farba_zelena, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
#Menu
def menu():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg, (0, 0))
        text_obrazovky("PLAY", farba_biela, 360, 210)
        text_obrazovky("LEADERBOARD", farba_biela, 300, 315)
        text_obrazovky(" EXIT", farba_biela, 355, 505)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP3:
                    zrusit_hru = True
                    quit()
                if event.key == pygame.K_KP1:
                    menu_levely()
            if event.type == pygame.QUIT:
                zrusit_hru = True
                pygame.quit()
                quit()
def menu_levely():
    zrusit_hru = False
    while not zrusit_hru:
        screen.blit(bg2, (0, 0))
        text_obrazovky("CLASSIC", farba_biela, 330, 202)
        text_obrazovky("MULTI APPLE", farba_biela, 305, 287)
        text_obrazovky("LEVEL 3", farba_biela, 335, 375)
        text_obrazovky("BACK", farba_biela, 350, 522)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    game()
                if event.key == pygame.K_KP2:
                    game2()
                if event.key == pygame.K_KP3:
                    game3()
                if event.key == pygame.K_KP4:
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()
menu()

