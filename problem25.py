# Find the index of the first number in the fibo sequence that has more than 1000 digits 
import math
import sys
sys.setrecursionlimit(10000)
numDigits = 1

number = 1
def getFib(index):
	index -= 2
	i = 0
	val1 = 1
	val2 = 1
	while(i < index):
		temp = val2
		val2 += val1
		val1 = temp
		i += 1

	return val2



def main():
	# print getFib(100) % 10**100;
	print math.log(getFib(4782),10) + 1
if __name__ == "__main__":
	main();