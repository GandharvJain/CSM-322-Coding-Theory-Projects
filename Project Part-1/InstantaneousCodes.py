def parseInput(d):
	codewords = list()
	pairs = d.strip().strip('{}').split(',')
	for i in pairs:
		pair = i.split(':')
		codewords.append(pair[1].strip().strip('\''))
	return codewords


raw_input = input("Enter encoding (Ex - {A: '1', B: '0'}): ")
codewords = parseInput(raw_input)
codewords.sort(key = len)

n = len(codewords)

# Check if a codeword is prefix of another
for i in range(n):
	for j in range(i + 1, n):
		c1 = codewords[i]
		c2 = codewords[j]

		if c2.startswith(c1):
			print("No, {} has prefix {}".format(c2, c1))
			exit()

print("Yes")