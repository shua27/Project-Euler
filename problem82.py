
def getArray():
	matrix = [[0 for x in range(80)] for x in range(80)] 
	file = open("matrix.txt")

	for line in file:
		print line.split(",")
		matrix.append(line.split(','))	

def main():
	list = getArray()
	print list

if __name__ == "__main__":
	main()