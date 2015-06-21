# Find the millionth lexicographic permutation of  0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
list = ['0','1','2','3','4','5','6','7','8','9']

def foo():
	count = 0
	for a in range (10): 									#1 
		for b in range(9):		       				        #2 
			for c in range(8): 								#3 
				for d in range(7): 							#4  
					for e in range(6): 		 				#5 
						for f in range(5):				    #6 
							for g in range(4): 				#7 
								for h in range(3):	    	#8 
									for i in range(2):	 	#9 
										for j in range(1): #10
											count += 1;
											if count > 999999:
												print a,b,c,d,e,f,g,h,i,j
												return count

def main():
	foo()

if __name__ == "__main__":
	main()
2783915460
2783915460

# ['0','1','3','4','5','6','7','8','9']
# ['0','1','3','4','5','6','8','9']
# ['0','1','3','4','5','6','9']
# ['0','1','4','5','6','9']
# ['0','1','4','5','6']
# ['0','4','5','6']
# ['0','4','6']
# ['0','6']
# ['0']
# []






