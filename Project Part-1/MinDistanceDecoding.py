def parseInput(d):
	d, recv_word = d.strip().rsplit(',', 1)
	recv_word = recv_word.strip()
	elements = d.strip().strip('{}').split(',')
	codewords = list()
	for i in elements: codewords.append(i.strip())
	return recv_word, codewords

def HammingDistance(x, y):
	ans = 0
	ans += 1 for i in range(len(x)) if x[i] != y[i]
	return ans

recv_word, codewords = parseInput(input("Enter encoding (Ex - {000, 111}, 110): "))

sent_word = ""
min_hamming_distance = len(recv_word) + 1
for c in codewords:
	t = HammingDistance(recv_word, c)
	if min_hamming_distance > t:
		sent_word = c
		min_hamming_distance = t

print(f"Most likely codeword sent using MDD rule: {sent_word}")