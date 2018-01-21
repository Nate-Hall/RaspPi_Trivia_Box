import pygame
import msvcrt

pygame.init()
pygame.joystick.init()
for i in range(pygame.joystick.get_count()):
    pygame.joystick.Joystick(i).init()

lockoutDelay = 3.0
lockoutCountdown = 0.0

currentButton = -1
currentJoy = -1

lastTime = time.time()

def mainLoop():
	while(True):
		if(lockoutCountdown <= 0):
			for event in pygame.event.get(): # User did something
				# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		        if event.type == pygame.JOYBUTTONDOWN:
		        	currentPressed = event.dict['button']
		        	currentJoy = event.dict['joy']
		        	lockoutCountdown = lockoutDelay

		        	### Play appropriate sound
		        	### Turn on light

		else:
			lockoutCountdown -= (time.time() - lastTime)
			if(lockoutCountdown <= 0):
				### Turn off light
			else:
				### Keep light on


		if msvcrt.kbhit():
	        key = ord(readch())
	        if key == 27:  # escape key
	            break

		lastTime = time.time()

mainLoop()