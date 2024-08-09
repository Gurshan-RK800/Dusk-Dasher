import pygame
import sys

pygame.init()

# Set the display mode
screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))

# Load and scale down the sprite
sprite_character = pygame.image.load('./images/Leon sprite.png').convert_alpha()
sprite_character = pygame.transform.scale(sprite_character, (sprite_character.get_width() // 2, sprite_character.get_height() // 2))

bg_menu = pygame.image.load('./Images/dark.jpg')
game_background = pygame.image.load('./Images/Improved Woods.jpg')

# Initialize fonts
font = pygame.font.SysFont("Jaro", 60, bold=True, italic=True)
game_over_font = pygame.font.SysFont("Jaro", 80, bold=True, italic=True)

bg_width = game_background.get_width()
bg_height = game_background.get_height()

# Player setup
player_size = sprite_character.get_width()
player = pygame.Rect(600, 530 - player_size, player_size, player_size)

y_velocity = 0
gravity = 0.5  # Gravity force
jump_force = -15  # Increased jump force
on_ground = False  # To prevent double jumps

# Platform setup
platforms = [
    pygame.Rect(600, 550, 200, 20),  # First platform (player starts here)
    pygame.Rect(900, 450, 200, 20),  # Second platform
    pygame.Rect(1200, 350, 200, 20), # Third platform
    pygame.Rect(1500, 300, 200, 20), # Fourth platform
    pygame.Rect(1800, 250, 200, 20), # Fifth platform
]

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

# Function to display game over screen
def display_game_over():
    screen.fill((0, 0, 0))
    write('Game Over... Better Luck Next Time..', game_over_font, (255, 0, 0), 250, screen_height // 2)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds before exiting

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
    global player, y_velocity, on_ground

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

        # Apply gravity
        y_velocity += gravity
        player.y += y_velocity

        # Check if the player falls off the screen
        if player.bottom >= screen_height:
            display_game_over()
            return  # Exit game_loop

        # Platform collision (only if falling)
        on_ground = False  # Reset on_ground status
        for platform in platforms:
            if player.colliderect(platform) and y_velocity > 0:
                if player.bottom > platform.top and player.bottom <= platform.bottom:
                    player.bottom = platform.top
                    y_velocity = 0  # Stop falling when on the platform
                    on_ground = True

        # Jumping
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and on_ground:
            y_velocity = jump_force  # Jump only when the player is on the ground or a platform
            on_ground = False

        # Horizontal movement and camera adjustment
        if key[pygame.K_a]:
            player.x -= 5
            if player.left < screen_width // 2:
                camera_x -= 5  # Adjust camera position
        if key[pygame.K_d]:
            player.x += 5
            if player.right > screen_width // 2:
                camera_x += 5  # Adjust camera position

        # Center camera on player
        camera_x = min(max(camera_x, 0), bg_width * 2 - screen_width)
        camera_y = min(max(camera_y, 0), bg_height * 2 - screen_height)

        # Draw the player sprite
        screen.blit(sprite_character, (player.x - camera_x, player.y - camera_y))

        # Draw the platforms
        for platform in platforms:
            pygame.draw.rect(screen, (144, 238, 144), (platform.x - camera_x, platform.y - camera_y, platform.width, platform.height))  # Light green color for platforms

        pygame.display.update()

        # Event handling
        handle_game_events()

        pygame.display.update()
        pygame.time.Clock().tick(60)  # Frame rate limit

# Main function to run the program
def main():
    main_menu()  # Show the main menu
    game_loop()  # Start the game

main()


