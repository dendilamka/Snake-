import pygame
import random
#intialize the pygame
pygame.init()
#ROZLÍŠENIE
res = (800, 600)
#OTVORIŤ OKNO
screen = pygame.display.set_mode(res)
#ŠÍRKA A VÝŠKA
sirka = screen.get_width()
vyska = screen.get_height()
#NÁZOV a Icona
pygame.display.set_caption("Snake")
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
font1 = pygame.font.SysFont("Eras Bold ITC", 40)
#TEXTY
def text_obrazovky(text, farba, x, y):
    text_obrazovky = font1.render(text, True, farba)
    screen.blit(text_obrazovky, [x,y])

def snake (screen, farba, list, velkost_hada):
    for x,y in list:
        pygame.draw.rect(screen, farba, [x,y, velkost_hada, velkost_hada])

#HRA
def game():
    zrusit_hru = False
    koniec_hry = False
    snake_x = 45
    snake_y = 55
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
            screen.fill(farba_siva_tmava)
            text_obrazovky("Prehral si, stlač ENTER pre pokračovanie", farba_cervena, 120, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zrusit_hru = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - jablko_x) < 10 and abs(snake_y - jablko_y) < 10:
                score += 1
                jablko_x = random.randint(20, sirka - 30)
                jablko_y = random.randint(60, vyska - 30)
                dlzka += 5

            screen.fill(farba_siva_tmava)
            text_obrazovky("Score: " + str(score * 10), farba_cierna, 10, 5)
            pygame.draw.rect(screen, farba_cervena, [jablko_x, jablko_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_cierna, (0, 40), (800, 40), 5)


            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                koniec_hry = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                koniec_hry = True
            snake(screen, farba_zelena, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

game()














