import pygame

# initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Move the ball with arrow keys")

# set up the ball
ball_color = (255, 0, 0)
ball_pos = [225, 225]  # initial position
ball_radius = 25

# define a function to draw the ball
def draw_ball():
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN:
                ball_pos[1] += 20
            elif event.key == pygame.K_LEFT:
                ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] += 20
    
    # check if ball is out of screen bounds
    if ball_pos[0] < ball_radius:
        ball_pos[0] = ball_radius
    elif ball_pos[0] > 500 - ball_radius:
        ball_pos[0] = 500 - ball_radius
    if ball_pos[1] < ball_radius:
        ball_pos[1] = ball_radius
    elif ball_pos[1] > 500 - ball_radius:
        ball_pos[1] = 500 - ball_radius
    
    # draw the screen
    screen.fill((255, 255, 255))
    draw_ball()
    pygame.display.flip()

# quit pygame
pygame.quit()
