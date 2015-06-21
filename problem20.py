import sys
sys.setrecursionlimit(10000)
def fact(n):
	if n == 1:
		return n
	else: 	
		return n * fact(n-1)

def sumDigits(n):
	s = str(n)
	sum = 0
	for i in range(0, len(s)):
		sum += int(s[i])
	return sum;
def main():
	print sumDigits(fact(100))

if __name__ == "__main__": main()