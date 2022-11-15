import numpy as np
q = 2

def modInv(a):
	for x in range(1, q):
		if (a * x) % q == 1: return x

def swapCol(A, i, j):
	A[:, i], A[:, j] = A[:, j], A[:, i].copy()

def rref(G):
	m, n = G.shape
	i, j = 0, 0

	rank = 0
	while i < m and j < n:
		t = np.argmax(G[i:m, j]) + i
		p = G[t, j]
		if p == 0:
			j += 1
			continue

		rank += 1
		if i != t:
			G[[i, t]] = G[[t, i]]

		G[i] *= modInv(G[i, j])
		G[i] %= q

		for l in range(m):
			if l != i:
				G[l] -= G[l, j] * G[i]
				G[l] %= q

		i += 1
		j += 1
	return G[:rank]

def generatorToParityCheck(G):
	swaps_seq = []
	k, n = G.shape
	j = 0
	for i in range(k):
		if G[i, i] != 1:
			while j < n:
				j += 1
				if G[i, j] == 1:
					break
			swapCol(G, i, j)
			swaps_seq.append((i, j))

	X = G[:,k:n]
	H = np.concatenate((-1*X.T % q, np.identity(n - k, int)), axis=1)
	for s in reversed(swaps_seq):
		swapCol(H, s[0], s[1])
	return H

def main():
	S = input("Enter codewords (space-seperated): ").strip().split()
	G = np.array([list(c) for c in S], int)
	G = rref(G)
	print(f'G = \n{G}\n')
	H = generatorToParityCheck(G)
	print(f'H = \n{H}\n')
	return G, H

if __name__ == '__main__':
	main()