''' Write a Python program that writes out a table of 
the function sin(x) vs. x, where x is tabulated 
between 0 and 2 with a thousand entries. Follow the 
basic Python program structure, including a main 
program function.'''

#import numpy for sin(x)
import numpy as np


def funct():
	#make array of 0-2 with a thousand entires
	n = 1000
	arr = np.linspace(0,2,n)

	#for each item in array
	i = 0.0
	for x in arr:
		#calculate the sin of x
		i = np.sin(x)
		#print out both sin and x values
		print(f"{i:1.16f} | {x}")



#define main function
def main():
	#set up table
	print("            sin(x) vs. x")
	print("------------------------------------------")
	#call function that prints out rest of table
	funct()


if __name__ == '__main__':
	main()






