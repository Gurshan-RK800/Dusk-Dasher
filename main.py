import pygame
import sys

pygame.init()

screen_height = 720
screen_width = 1280

player_size = 50
player = pygame.Rect(screen_width // 2, screen_height // 2, player_size, player_size)
# Font
font = pygame.font.SysFont("Jaro", 60, bold=True, italic=True)

screen = pygame.display.set_mode((screen_width, screen_height))

bg_menu = pygame.image.load('./Images/dark.jpg')

game_background = pygame.image.load('./Images/Improved Woods.jpg')
bg_width = game_background.get_width()
bg_height = game_background.get_height()


# Function to display menu
def display_menu():
    screen.blit(bg_menu, (0, 0))
    write('Main Menu', font, (255, 255, 255), 550, 100)
    write('Start Game', font, (255, 255, 255), 550, 250)
    write('Quit', font, (255, 255, 255), 600, 360)


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
                if 550 <= mouse_pos[0] <= 750 and 250 <= mouse_pos[1] <= 310:
                    return 'start_game'
                elif 600 <= mouse_pos[0] <= 800 and 360 <= mouse_pos[1] <= 420:
                    pygame.quit()
                    sys.exit()


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
            sys.exit()


# Game loop
def game_loop():
    global player

    camera_x, camera_y = 0, 0  # Initial camera position

    while True:
        screen.fill((0, 0, 0))

        # Calculate the background position based on the camera position
        offset_x = camera_x % bg_width
        offset_y = camera_y % bg_height

        # Draw the background images to create the infinite scrolling effect
        for i in range(-1, screen_width // bg_width + 2):
            for j in range(-1, screen_height // bg_height + 2):
                screen.blit(game_background, (i * bg_width - offset_x, j * bg_height - offset_y))

        # Draw the player
        screen.blit(game_background, (i * bg_width - offset_x, j * bg_height - offset_y))
        pygame.draw.rect(screen, (255, 0, 0), player)

        pygame.display.update()

        # Event handling
        handle_game_events()

        # Movement
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player.x -= 5
            if player.left < 0:
                player.left = 0
                camera_x -= 5
        if key[pygame.K_d]:
            player.x += 5
            if player.right > screen_width:
                player.right = screen_width
                camera_x += 5
        if key[pygame.K_s]:
            player.y += 5
            if player.bottom > screen_height:
                player.bottom = screen_height
                camera_y += 5
        if key[pygame.K_w]:
            player.y -= 5
            if player.top < 0:
                player.top = 0
                camera_y -= 5

        pygame.display.update()


# Main function to run the program
def main():
    main_menu()  # Show the main menu
    game_loop()  # Start the game


main()
