def buildMatrix():
	matrix = Matrix = [[0 for x in range(20)] for x in range(20)] 
	with open("grid.txt") as fd:
		for index, line in enumerate(fd):
			Matrix[index] = line.split()


	for i in range (0,20):
		for j in range (0,20):
			matrix [i][j] = int(matrix[i][j])
	return matrix

def getMax(matrix):
	maxProduct = 0
	# Check left and right solutions 
	for i in range (0,20):
		for j in range(0,17):
			product = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3] 
			if product > maxProduct:
				maxProduct = product

	# Check up and down solutions 
	for i in range (0,17):
		for j in range(0,20):
			product = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j] 
			if product > maxProduct:
				maxProduct = product

	# Check forward Diagonals
	for i in range(0,17):
		for j in range(0,17):
			product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3] 
			if product > maxProduct:
				maxProduct = product


	# Check Backward diagonals
	for i in range(0,17):
		for j in range(3,20):
			product = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3] 
			if product > maxProduct:
				print i,j
				maxProduct = product

	return maxProduct

def main():
	matrix = buildMatrix()
	print getMax(matrix)

if __name__ == "__main__":
	main()
	