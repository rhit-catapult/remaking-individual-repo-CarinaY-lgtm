import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  ) ** is exponent
    return math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)
    


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    # 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer.music.load("03-ClickInTheCircle/drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = "" # blank message that can change


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = pygame.mouse.get_pos()
                distance_from_center = distance(click_position, circle_center)
                if distance_from_center <= circle_radius:
                    print("Start the music!")
                    message_text = "Bullseye!"
                    pygame.mixer.music.play(-1) # -1 means loop forever
                else:
                    print("Stop the music!")
                    message_text = "You missed!"
                    pygame.mixer.music.stop()
                
                    

        screen.fill(pygame.Color("Black"))

        # 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        # 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        caption = font.render(message_text, True, (122, 237, 201))

    # positions for instruction text
        screen.blit(instructions_image, (25, 25))
  
        #  7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'
        screen.blit(caption, (25, 50)) 

        pygame.display.update()


main()
