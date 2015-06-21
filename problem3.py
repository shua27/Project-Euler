# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math;
import sys
sys.setrecursionlimit(10000)
def is_prime(n):
	  if n == 2 or n == 3: return True
	  if n < 2 or n%2 == 0: return False
	  if n < 9: return True
	  if n%3 == 0: return False
	  r = int(n**0.5)
	  f = 5
	  while f <= r:
	    if n%f == 0: return False
	    if n%(f+2) == 0: return False
	    f +=6
	  return True

def findPrime(number):
	start = number/2;
	math.trunc(start);

	if (start % 2 == 0):
		start += 1;

	print start;

	while start > 0:
		if number % start == 0 & is_prime(start):
			return start;
		else: start -= 2;

def printPrimes(num):
	primefound = 1;
	for i in range(2,100000):
		
		if (num%i == 0):
			primefound = 0
			candidate = num/i
			printPrimes(candidate);
	
	if is_prime(num):
		print num
def main():
	print printPrimes(600851475143);

if __name__ == "__main__": main()