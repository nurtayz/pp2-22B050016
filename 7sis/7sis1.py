import pygame
import time
import math
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()
mickey_img = pygame.image.load("mickey5565.png")
mickey_rect = mickey_img.get_rect()
mickey_rect.center = (200, 200)
def rotate_hand(angle, length):
    x = math.sin(math.radians(angle)) * length
    y = -math.cos(math.radians(angle)) * length
    return (x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Get the current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    # Rotate the hands based on the current time
    seconds_angle = seconds * 6
    minutes_angle = minutes * 6
    
    seconds_hand = rotate_hand(seconds_angle, 80)
    minutes_hand = rotate_hand(minutes_angle, 60)
    
    # Draw the hands on the screen
    screen.fill((255, 255, 255))
    mickey_rect.centerx += minutes_hand[0]
    mickey_rect.centery += minutes_hand[1]
    screen.blit(pygame.transform.rotate(mickey_img, -minutes_angle), mickey_rect)
    mickey_rect.centerx += seconds_hand[0]
    mickey_rect.centery += seconds_hand[1]
    screen.blit(pygame.transform.rotate(mickey_img, -seconds_angle), mickey_rect)
    
    pygame.display.update()
    clock.tick(60)
