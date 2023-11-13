''' 
Session 3 Prompt: Write a Python program that defines a 
function f(x) that returns x**3 + 8. In the main function of 
the program, call f(x) with x = 9 and print the result.
Use an if statement that executes if the result is larger
than 27 and prints “YAY!”.

'''

def Function(x):
	#calculate
	res = x**3 + 8
	return res



def main():
	#call function with x = 9
	x = Function(9)
	print("\nresult of 9**3 + 8: ", x)
	#check equality of x and 27
	#if equal print "YAY!
	if(x > 27):
		print("YAY!\n")
	else:
		print("oh no!\n")


#executing the main function
if __name__=="__main__":
	main()