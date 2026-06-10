# The two lines below allow you to use PyGame and System functions.
# Often programmers use code that other developers have written.
import pygame
import sys

# Let's turn pygame ON. init means initialize
pygame.init()

pygame.display.set_caption("Carina Yang")
screen = pygame.display.set_mode((750, 650))

while True:
    for event in pygame.event.get():
        print(event)

        # This is a conditional statement, i.e., the line sys.exit() will ONLY
        # execute when event.type is equal to pygame.QUIT (this is what ==
        # means). 
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events
 
    screen.fill(pygame.Color("Grey"))

    # Draw things on the screen (colour, coordinates, radius, optional thickness/width)
    # colour (R, G, B) highest is 255, lowest is 0
    # coordinates (0,0) is top left corner, positive x goes right, positive y goes down
    # don't hard-code numbers, use screen.get_width() and screen.get_height() 
    pygame.draw.circle(screen, pygame.Color("Purple"), (screen.get_width() / 2, screen.get_height() / 2), 100)
    pygame.draw.circle(screen, (255, 80, 50), (screen.get_width() - 150, screen.get_height() - 170), 80, 10)
    pygame.draw.circle(screen, (255, 255, 0), (150, screen.get_height() - 150), 50)

    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()