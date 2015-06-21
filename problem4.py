# The largest palindrome that is a product of two 3-digit numbers
import string
def isPalindrome(string):
	firstHalf = ""
	secondHalf = ""
	length = len(string)
	
	if length % 2 == 0:
		firstHalf = string[0:length/2]
		secondHalf = string[length/2:length]
	else:
		firstHalf = string[0:length/2]
		secondHalf = string[length/2+1:length]

	secondHalf = secondHalf[::-1]

	if firstHalf == secondHalf:
		return "TRUE";

def main():
	maxPalindrome = 0

	for i in range(100,999):
		for j in range(100,999):
			palindrome = i*j 
			if (isPalindrome(str(palindrome)) == "TRUE")  & (palindrome > maxPalindrome):
				maxPalindrome = palindrome

	print maxPalindrome
if __name__ == "__main__":
	main()