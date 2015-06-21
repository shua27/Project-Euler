# 
import string
def getDivisors(num):
	list = []
	max = num / 2 + 1 
	i = 1;
	while i <= max:
		if num % i == 0:
			list.append(i)
		i += 1
	list.append(num)
	return list

def main():
	print getDivisors(15 10)

if __name__ == "__main__":
	main()