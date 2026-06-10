import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    eye_x = 0
    eye_y = 0

    while True:
        # TODO 4: Set the clock speed to 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys

            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    print("up")
                    eye_y -= 5
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_DOWN]:
                    print("down")
                    eye_y += 5

            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_LEFT]:
                    print("left")
                    eye_x -= 5
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_RIGHT]:
                    print("right")
                    eye_x += 5



        screen.fill((255, 255, 255))  # white

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (240 + eye_x, 160 + eye_y), 10)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (400 + eye_x, 160 + eye_y), 10)  # black pupil

        pygame.draw.circle(screen, (80, 30, 0), (320, 245), 10) # brown nose 

        pygame.draw.rect(screen, (255,50,10), (230, 320, 180, 30),) # mouth
        pygame.draw.rect(screen, (0,0,0), (230, 320, 180, 30), 5) # black outline


        pygame.display.update()


# call  to main function, if removed the program won't run
main()
