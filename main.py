import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coordinate to WASD Emulation")


# Function to emulate key press based on coordinates
def emulate_key_press(x, y):
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2

    # Calculate the angle relative to the center
    dx = x - center_x
    dy = center_y - y  # Invert y to match traditional coordinate system
    angle = math.degrees(math.atan2(dy, dx))
    if angle < 0:
        angle += 360

    # Determine the octant
    if 337.5 <= angle or angle < 22.5:  # "d"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d))
        print('d')
    elif 22.5 <= angle < 67.5:  # "wd"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d))
        print('wd')
    elif 67.5 <= angle < 112.5:  # "w"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w))
        print('w')
    elif 112.5 <= angle < 157.5:  # "wa"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))
        print('wa')
    elif 157.5 <= angle < 202.5:  # "a"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))
        print('a')
    elif 202.5 <= angle < 247.5:  # "as"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s))
        print('as')
    elif 247.5 <= angle < 292.5:  # "s"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s))
        print('s')
    elif 292.5 <= angle < 337.5:  # "sd"
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d))
        print('sd')


# Main loop
def main():
    running = True

    # Initialize x and y coordinates
    x = 0
    y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Emulate key press based on coordinates
        emulate_key_press(x, y)

        # Update the display
        # pygame.display.flip()

        # Cap the frame rate
        # pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
