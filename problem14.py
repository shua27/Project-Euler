def handleEven(n):
	return n/2

def handleOdd(n):
	return 3*n + 1

def main():
	maxChain = 0
	maxChainSeed = 0
	chainLength = 0

	startSeed = 500001
	while startSeed < 1000000:
		seed = startSeed
		while (seed != 1):
			if (seed % 2 == 0):
				seed /= 2
			else
:				seed = seed * 3 + 1
			
			chainLength += 1
		
		if(chainLength > maxChain):
			maxChain = chainLength
			maxChainSeed = startSeed
		
		chainLength = 0
		startSeed += 2

	print maxChainSeed

if __name__ == "__main__": main()