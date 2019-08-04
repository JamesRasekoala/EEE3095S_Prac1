#!/usr/bin/python3
"""
Names: James Rasekoala
Student Number: RSKJAM001
Prac: EEE3095S Prac 1
Date: 22/07/2019

"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#button setup
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#initial variables
count = 0

#LED setup
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#debouncing method for counting up
def countup():
	global count	#To uses global count value in method
	input_state = GPIO.input(12)	#button at pin 12
	if input_state == False:
		#count up increment
		count = count+1
		print("Count UP Pressed")	
		Config_Led(count)	#Adjusts Led configuration


#debouncing method for counting down
def countdown():
	global count	#To uses global count value in method
	input_state = GPIO.input(16)	#button at pin 16
	if input_state == False:
		#count down decrement
		count = count-1
		print("Count Down Pressed")
		Config_Led(count)	#Adjusts Led configuration


#count limitations
def check_counter(counter):
	global count	#To uses global count value in method
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
		print(counter)
		

	elif(counter == 1):
		GPIO.output(18,True)
		GPIO.output(23,False)
		GPIO.output(24,False)
		print(counter)
		

	elif(counter == 2):
		GPIO.output(18,False)
		GPIO.output(23,True)
		GPIO.output(24,False)
		print(counter)

		
	elif(counter == 3):
		GPIO.output(18,True)
		GPIO.output(23,True)
		GPIO.output(24,False)
		print(counter)
		

	elif(counter == 4):
		GPIO.output(18,False)
		GPIO.output(23,False)
		GPIO.output(24,True)
		print(counter)
		
		
	elif(counter == 5):
		GPIO.output(18,True)
		GPIO.output(23,False)
		GPIO.output(24,True)
		print(counter)


	elif(counter == 6):
		GPIO.output(18,False)
		GPIO.output(23,True)
		GPIO.output(24,True)
		print(counter)
		

	elif(counter == 7):
		GPIO.output(18,True)
		GPIO.output(23,True)
		GPIO.output(24,True)
		print(counter)

def main():
	
	countdown()
	countup()


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
