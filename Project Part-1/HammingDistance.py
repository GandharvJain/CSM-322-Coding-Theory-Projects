def parseInput(d):
	elements = d.strip().strip('{}').split(',')
	codewords = []
	for i in elements:
		codewords.append(i.strip())
	return codewords

def HammingDistance(x, y):
	ans = 0
	for i in range(32):
		b1 = (x>>i)&1
		b2 = (y>>i)&1
		if b1 != b2:
			ans += 1

	return ans


raw_input = input("Enter encoding (Ex - {1, 3, 5}): ")
codewords = parseInput(raw_input)

n = len(codewords)

s = sum(HammingDistance(i, j) for i in range(n) for j in range(n))
print(f"Sum of Hamming distances: {s}")