import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    stop = input("Press 's' to stop the music: ")
    if stop == "s":
      pause()
      return
    else:
      continue

while True:
  os.system("clear")
  print("replit music player")
  time.sleep(1)
  print("Press 'p' to play the music")
  print("Press 'e' to exit the program")
  print("Press anything else to see the music again")
  # Show the menu
  menu = input("")
  if menu == "p":
    print("Playing some proper tunes!")
    play()
  elif menu == "e":
    exit()
  else:
    continue
