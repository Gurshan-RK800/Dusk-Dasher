import pygame
import sys

pygame.init()

screen_height = 800
screen_width = 1000

# Font
font = pygame.font.SysFont("Jaro", 60, bold=True, italic=True)

screen = pygame.display.set_mode((screen_width, screen_height))

forest_background = pygame.image.load('./Images/redleaves.jpg')

# Function to display menu
def display_menu():
    screen.blit(forest_background, (0, 0))
    write('Main Menu', font, (0, 0, 0), 400, 100)
    write('Start Game', font, (0, 0, 0), 400, 250)
    write('Quit', font, (0, 0, 0), 450, 360)

# Function to write text on screen
def write(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Function to handle menu events
def handle_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if 400 <= mouse_pos[0] <= 600 and 250 <= mouse_pos[1] <= 310:
                    return 'start_game'
                elif 450 <= mouse_pos[0] <= 550 and 360 <= mouse_pos[1] <= 420:
                    pygame.quit()



# Main menu loop
def main_menu():
    while True:
        screen.fill((0, 0, 0))
        display_menu()
        pygame.display.update()
        action = handle_menu_events()
        if action == 'start_game':
            break

# Function to handle game events
def handle_game_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Game loop
def game_loop():
    while True:
        screen.fill((0, 0, 0))  # Clear the screen
        # Your game logic here
        handle_game_events()
        pygame.display.update()

# Main function to run the program
def main():
    main_menu()  # Show the main menu
    game_loop()  # Start the game

main()