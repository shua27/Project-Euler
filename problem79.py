def getLogs():
	file = open("keylog.txt")
	list = []; 
	for line in file:
		list.append(int(line))

	return list;

def swap(c, i, j):
  c = list(c)
  c[i], c[j] = c[j], c[i]
  return ''.join(c)

def analyzeLogs(logs):
	passphrase = "";

	for log in logs:
			letter1 = str(log)[0]
			letter2 = str(log)[1]
			letter3 = str(log)[2]

			if not letter1 in passphrase:
				passphrase = passphrase + letter1
			if not letter2 in passphrase:
				passphrase = passphrase + letter2
			if not letter3 in passphrase:
				passphrase = passphrase + letter3

			index1 = passphrase.index(letter1);
			index2 = passphrase.index(letter2);
			index3 = passphrase.index(letter3);

			if index1 > index2:
				passphrase = swap(passphrase, index1, index2)
			if index1 > index3:
				passphrase = swap(passphrase, index1, index3)
			if index2 > index3:
				passphrase  = swap(passphrase, index2, index3)

			print passphrase
	print passphrase

def main():
	logs = getLogs();
	analyzeLogs(logs);

if __name__ == "__main__":
	main();