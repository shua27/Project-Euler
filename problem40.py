MAX = 2000000

string = ""
i = 0
while i < 200000 :
	string = string + str(i)
	i += 1
sum = 1

sum *= int(string[1])
sum *= int(string[10])
sum *= int(string[100])
sum *= int(string[1000])
sum *= int(string[10000])
sum *= int(string[100000])
sum *= int(string[1000000])


print sum