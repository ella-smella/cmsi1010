import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHAPE_WIDTH = 200
SHAPE_HEIGHT = 150
BORDER_THICKNESS = 3
SHAPE_FILL_COLOR = (175, 159, 82)
SHAPE_BORDER_COLOR = (137, 131, 59)
BACKGROUND_COLOR = (255, 235, 179)

# Always begin with initialization, sizing, and captioning
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('rectangle :3')

# A best practice is to do the drawing in its own function
def draw_scene():
    screen.fill(BACKGROUND_COLOR) 
    the_rectangle = ((SCREEN_WIDTH - SHAPE_WIDTH) // 2, (SCREEN_HEIGHT - SHAPE_HEIGHT) // 2, SHAPE_WIDTH, SHAPE_HEIGHT)  # (x, y, width, height)
    pygame.draw.rect(screen, SHAPE_FILL_COLOR, the_rectangle)  # filled
    pygame.draw.rect(screen, SHAPE_BORDER_COLOR, the_rectangle, BORDER_THICKNESS)  # outlined
    pygame.display.flip()  # Put the drawing on the screen


# Draw the scene then wait for the QUIT event to come in
draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit