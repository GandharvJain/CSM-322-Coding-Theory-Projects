def parseInput(d):
	elements = d.strip().strip('{}').split(',')
	codewords = list()
	for i in elements: codewords.append(i.strip())
	return codewords

def HammingDistance(x, y):
	ans = 0
	for i in range(32):
		if (x>>i)&1 != (y>>i)&1: ans += 1
	return ans

codewords = parseInput(input("Enter encoding (Ex - {1, 3, 5}): "))
n = len(codewords)
s = sum(HammingDistance(i, j) for i in range(n) for j in range(n))

print(f"Sum of Hamming distances: {s}")