'''
Session 4 Prompt: Write a Python program that declares a class
describing your favorite animal. Have the data members of the 
class represent the following physical parameters of the 
animal: length of the arms (float), length of the legs (float), 
number of eyes (int), does it have a tail? (bool), is it furry? 
(bool). Write an initialization function that sets the values 
of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe 
the data members representing the physical characteristics of 
the animal.

'''

import sys

class Panda: #declaring class
	#print out description on animal
	def print(self):
		print("\nMy favorite animal is a Panda")
		print(f"It's arms are about {self.num_arms} inches long")
		print(f"It's legs are about {self.num_legs} inches long")
		print(f"It has {self.num_eyes} eyes")
		if(self.has_tail == True):
			print(f"It does have a tail")
		else:
			print("It does not have a tail")

		if(self.is_furry == True):
			print(f"It is furry")
		else:
			print("It is not furry")

		print("\n")

	#init functions to set values of data members
	def __init__(self, arms=1.0, legs=1.0, eyes=2, tail=True, furry=True):
		self.num_arms = arms
		self.num_legs = legs
		self.num_eyes = eyes
		self.has_tail = tail
		self.is_furry = furry

def main():

	#set data members for animal attributes
	#with default data
	arms = 26.5
	legs = 25.0
	eyes = 2
	tail = True
	furry = True
	#set values of data members
	animal = Panda(arms=arms,legs=legs,eyes=eyes,tail=tail,furry=furry)
	#print out description
	animal.print()

if __name__=="__main__":
	main()


