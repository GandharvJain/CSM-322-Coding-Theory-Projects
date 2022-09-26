def parseInput(d):
	d, recv_word = d.strip().rsplit(',', 1)
	recv_word = recv_word.strip()
	elements = d.strip().strip('{}').split(',')
	codewords = []
	for i in elements:
		codewords.append(i.strip())
	return recv_word, codewords

def HammingDistance(x, y):
	ans = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			ans += 1
	return ans

raw_input = input("Enter encoding (Ex - {000, 111}, 110): ")
recv_word, codewords = parseInput(raw_input)

sent_word = ""
min_hamming_distance = len(recv_word) + 1
for c in codewords:
	t = HammingDistance(recv_word, c)
	if min_hamming_distance > t:
		sent_word = c
		min_hamming_distance = t


print(f"Most likely codeword sent using MDD rule: {sent_word}")