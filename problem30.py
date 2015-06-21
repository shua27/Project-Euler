#problem30
EXP = 5
MAXNUM = 10**7

class numberList:
	number = 0
	list = []
	bool = 0
	sum = 0

	def __init__(self, number):
		self.number = number
		self.list = getDigits(number)
		check(self)

def check(numberList):

	for num in numberList.list:
		numberList.sum += num**EXP

	if numberList.sum == numberList.number:
		numberList.bool = 1

def getDigits(num):
	list = []
	while num > 0: 
		list.append(num % 10)
		num = num/10
	return list;

def main():
	sum = -1
	i = 0
	while i < MAXNUM:
		test = numberList(i)
		if test.bool == 1:
			sum += i
			print sum
		i += 1
if __name__ == "__main__":
	main()