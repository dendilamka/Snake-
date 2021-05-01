import pygame
import random
#intialize the pygame
pygame.init()
#ROZLÍŠENIE
res = (800, 700)
#OTVORIŤ OKNO
screen = pygame.display.set_mode(res)
#ŠÍRKA A VÝŠKA
sirka = screen.get_width()
vyska = screen.get_height()
#NÁZOV
pygame.display.set_caption("Snake")
pygame.display.update()
clock = pygame.time.Clock()
#FARBY
farba_biela = (255, 255, 255)
farba_siva_svetla = (170, 170, 170)
farba_siva_tmava = (100, 100, 100)
farba_zelena = (0, 128, 0)
farba_modra = (0, 0, 255)
farba_cervena = (255, 0, 0)
farba_cierna = (0, 0, 0)

#FONT
font1 = pygame.font.SysFont('Corbel', 35)
#TEXTY
text_quit = font1.render("QUIT", True, farba_biela)
def text_obrazovky(text, farba, x, y):
    text_obrazovky = font1.render(text, True, farba)
    screen.blit(text_obrazovky, [x,y])

def snake (screen, farba, list, velkost_hada):
    for x,y in list:
        pygame.draw.rect(screen, farba, [x,y, velkost_hada, velkost_hada])

#HRA
def game():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    list = []
    dlzka = 1

    food_x = random.randint(20, sirka - 20)
    food_y = random.randint(60, vyska - 20)
    score = 0
    init_velocity = 4
    velkost_hada = 30
    fps = 60
    while not exit_game:
        if game_over:
            screen.fill(farba_siva_tmava)
            text_obrazovky("Prehral si, stlač ENTER pre pokračovanie", farba_cervena, 100, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

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

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                food_x = random.randint(20, sirka - 30)
                food_y = random.randint(60, vyska - 30)
                dlzka += 5

            screen.fill(farba_zelena)
            text_obrazovky("Score: " + str(score * 10), farba_cierna, 10, 5)
            pygame.draw.rect(screen, farba_cervena, [food_x, food_y, velkost_hada, velkost_hada])
            pygame.draw.line(screen, farba_cierna, (0, 40), (800, 40), 5)


            hlava = []
            hlava.append(snake_x)
            hlava.append(snake_y)
            list.append(hlava)

            if len(list) > dlzka:
                del list[0]

            if hlava in list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > sirka - 20 or snake_y < 50 or snake_y > vyska - 20:
                game_over = True
            snake(screen, farba_modra, list, velkost_hada)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

game()














