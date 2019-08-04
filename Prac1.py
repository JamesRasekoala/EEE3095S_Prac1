#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: James Rasekoala
Student Number: RSKJAM001
Prac: Prac 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

#initial variables
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 0
lighVal = 0
pressed = False
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setwarnings(False)

# 
def countup():
	global count
	input_state = GPIO.input(12)
	if input_state == False:
		#count up
		count = count+1
		pressed = True
		print("Count UP")
		Config_Led(count)
		time.sleep(1)

#
def countdown():
	global count
	input_state = GPIO.input(16)
	if input_state == False:
		#count down
		count = count-1
		pressed = True
		print("Count Down")
		Config_Led(count)
		time.sleep(1)

#count limitations
def check_counter(counter):
	global count
	counter = count
	if (count==-1):
		count = 7 # if less than 0 set to 7
	elif(count==8):
		count = 0 # if grater than 7 set to 0
		# if value within bounds it will continue 



#Method to display counter binary LED configuration		
def Config_Led(counter):
	#check and fix counter value 
	check_counter(counter)
	
	#statements to select correct LED configuration
	if(counter == 0):
		GPIO.output(18,False)
		GPIO.output(23,False)
		GPIO.output(24,False)
		pressed = False
		print("0")
		
	elif(counter == 1):
		GPIO.output(18,True)
		GPIO.output(23,False)
		GPIO.output(24,False)
		pressed =False
		print("1")
		
	elif(counter == 2):
		GPIO.output(18,False)
		GPIO.output(23,True)
		GPIO.output(24,False)
		pressed = False
		print("2")

		
	elif(counter == 3):
		GPIO.output(18,True)
		GPIO.output(23,True)
		GPIO.output(24,False)
		pressed = False
		print("3")
		
	elif(counter == 4):
		GPIO.output(18,False)
		GPIO.output(23,False)
		GPIO.output(24,True)
		pressed = False
		print("4")
		
		
	elif(counter == 5):
		GPIO.output(18,True)
		GPIO.output(23,False)
		GPIO.output(24,True)
		pressed = False
		print("5")

	elif(counter == 6):
		GPIO.output(18,False)
		GPIO.output(23,True)
		GPIO.output(24,True)
		pressed = False
		print("6")
		
	elif(counter == 7):
		GPIO.output(18,True)
		GPIO.output(23,True)
		GPIO.output(24,True)
		pressed = False
		print("7")

#GPIO.add_event_detect(12, GPIO.FALLING, callback=countup, bouncetime = 300)
#GPIO.add_event_detect(16, GPIO.FALLING, callback=countdown, bouncetime = 300)

# Logic that you write
def main():
	countup()
	countdown()

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
	while True:
		main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
