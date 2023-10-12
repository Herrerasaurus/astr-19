'''
Session 2 Prompt:
Write a Python that prints the sum of two floating point numbers,
the difference between two integers,
and the product of a floating point number and an integer.
In each case, have the program print out the data type
of the resulting answer.
'''

def math():

  #calculates the sum of two floating point nums
	##float values
	f1 = 2.5
	f2 = 3.6

	tot = f1 + f2

	###print out sum and data type
	print("\nthe sum of the two floating point numbers 2.5 and 3.6:")
	print(f1, "+", f2, "=", tot)
	print(type(tot))


	#calculates the difference between two integers
	##int values
	int1 = 36
	int2 = 15

	tot = int1 - int2

	###print out diff and data type
	print("\nthe difference between the two integers 36 and 15:")
	print(int1, "-", int2, "=", tot)
	print(type(tot))


	#calculates the product of a float and int
	##float values
	f1 = 17.3
	int1 = 8

	tot = f1 * int1

	###print out sum and data type
	print("\nthe product of the floating point number 17.3 and the integer 8:")
	print(f1, "*", int1, "=", tot)
	print(type(tot),"\n")


def main():
	math()

#executing the main function
if __name__=="__main__":
	main()
