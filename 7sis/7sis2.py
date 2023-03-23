import pygame
import os
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
music_dir = "music/"
music_files = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(".mp3")]
def play_music():
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()
current_track = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
    
    screen.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(60)
