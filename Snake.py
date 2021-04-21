import pygame
#intialize the pygame
pygame.init()
#ROZLÍŠENIE
res = (900,700)
#OTVORIŤ OKNO
screen = pygame.display.set_mode(res)
#ŠÍRKA A VÝŠKA
sirka = screen.get_width()
vyska = screen.get_height()
#NÁZOV
pygame.display.set_caption("Snake")
#FARBY
farba_biela = (255, 255, 255)
farba_siva_svetla = (170, 170, 170)
farba_siva_tmava = (100, 100, 100)
#FONT
font1 = pygame.font.SysFont('Corbel', 35)
#TEXTY
text_quit = font1.render("QUIT", True, farba_biela)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ZATVARANIE OKNA A TLACITKO QUIT                                                                              #///
while True:                                                                                                   #///
    for ev in pygame.event.get():                                                                             #///
        if ev.type == pygame.QUIT:                                                                            #///
            pygame.quit()                                                                                     #///
        if ev.type == pygame.MOUSEBUTTONDOWN:                                                                 #///
            if sirka / 2 <= mouse[0] <= sirka / 2 + 140 and vyska / 2 <= mouse[1] <= vyska / 2 + 40:          #///
                pygame.quit()                                                                                 #///
    screen.fill((65, 255, 141))                                                                               #///
    mouse = pygame.mouse.get_pos()                                                                            #///
    if sirka / 2 <= mouse[0] <= sirka / 2 + 140 and vyska / 2 <= mouse[1] <= vyska / 2 + 40:                  #///
        pygame.draw.rect(screen, farba_siva_tmava, [sirka / 2, vyska / 2, 140, 40])                           #///
    else:                                                                                                     #///
        pygame.draw.rect(screen, farba_siva_svetla, [sirka / 2, vyska / 2, 140, 40])                          #///
    screen.blit(text_quit, (sirka / 2 + 50, vyska / 2))                                                       #///
    pygame.display.update()                                                                                   #///
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

