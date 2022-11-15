import numpy as np
import A1to3_Linear as lin
q = 2

def genCodewords(codeword, indx, bits_left):
	C = []
	if bits_left > 0:
		for i in range(indx, len(codeword)):
			c = codeword.copy()
			c[i] = 1
			C += genCodewords(c, i + 1, bits_left - 1)
	else:
		C.append(codeword)
	return C

def syndromeTable(H):
	S = {}
	t, n = H.shape
	k = n - t
	total_syndromes = q ** (n - k)
	weight = 0
	
	while len(S) < total_syndromes:
		for u in genCodewords(np.zeros(n, int), 0, weight):
			S_u = u @ H.T
			if tuple(S_u) not in S:
				S[tuple(S_u)] = tuple(u)
		weight += 1
	return S

def decode(w, H_t, S_H):
	S_w = (w @ H_t) % q
	e = np.array([S_H.get(tuple(S_w))])
	u = (w - e) % q
	return u

def main():
	G, H = lin.main()
	w = np.array(list(input("Enter received word: ")), int)

	S_H = syndromeTable(H)
	sent_word = decode(w, H.T, S_H)

	print(f'Syndrome Table: {S_H}')
	print(f'Sent word: {sent_word}')

if __name__ == '__main__':
	main()