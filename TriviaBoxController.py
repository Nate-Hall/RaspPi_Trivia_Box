import pygame
import msvcrt
import time
from random import randint

pygame.init()
pygame.joystick.init()
for i in range(pygame.joystick.get_count()):
	pygame.joystick.Joystick(i).init()

def mainLoop():
	lockoutDelay = 2.0
	lockoutCountdown = 0.0

	currentButton = -1
	currentJoy = -1

	lastTime = time.time()
	newTime = time.time()

	playerChooser = -1

	while(True):
		if(lockoutCountdown <= 0):
			for event in pygame.event.get(): # User did something
				# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
				if event.type == pygame.JOYBUTTONDOWN:
					rand = randint(0, 99)
					if(rand >= playerChooser):
						playerChooser = rand
						currentButton = event.dict['button']
						currentJoy = event.dict['joy']
			if(playerChooser > -1):
				lockoutCountdown = lockoutDelay
				print (str(currentJoy) + str(currentButton))
				### Play appropriate sound
				### Turn on light

		else:
			if(lockoutCountdown <= (newTime - lastTime)):
				lockoutCountdown = 0
				currentButton = -1
				currentJoy = -1
				playerChooser = -1
				print("Reset")
				### Turn off light
			else:
				lockoutCountdown -= (newTime - lastTime)
				### Keep light on


		if msvcrt.kbhit():
			key = ord(msvcrt.getch())
			if key == 27:  # escape key
				break

		lastTime = newTime
		newTime = time.time()

mainLoop()