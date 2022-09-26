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
p = 0.05

sent_word = ""
max_fwd_prob = -1
for c in codewords:
	t = HammingDistance(recv_word, c)
	fwd_prob = (p ** t) * ((1 - p) ** (len(recv_word) - t))

	if max_fwd_prob < fwd_prob:
		sent_word = c
		max_fwd_prob = fwd_prob


print(f"Most likely codeword sent using MLD rule with p = {p}: {sent_word}")