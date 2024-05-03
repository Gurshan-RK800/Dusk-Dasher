import pygame, sys

pygame.init()

screen_height = 800
screen_width = 1000

#font
font = pygame.font.SysFont("Jaro", 60, bold = True, italic = True)

screen = pygame.display.set_mode((screen_width,screen_height))

game_paused = False
def write(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#game

run = True
while run:
    screen.fill((0, 0, 0))
    if game_paused == True:
        pass
    #display menu

    write('Main Menu', font, (128, 128, 128), 400, 100)
    write('Start Game', font, (128, 128, 128), 400,250)
    #quiting
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
