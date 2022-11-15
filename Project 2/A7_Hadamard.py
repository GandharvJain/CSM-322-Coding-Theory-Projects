import numpy as np
q = 2

def generateHadamard(n):
	H = [None] * (n + 1)
	H[0] = np.array([1], int)
	H[1] = np.array([[1, 1], [1, -1]], int)
	hadamard(H, n)
	return H

def hadamard(H, n):
	t = n - 1
	l = 2 ** t
	if H[n] is not None:
		return
	if H[t] is None:
		hadamard(H, t)

	H[n] = np.zeros((2**n, 2**n), int)
	H[n][:l, :l] = H[t]
	H[n][:l, l:] = H[t]
	H[n][l:, :l] = H[t]
	H[n][l:, l:] = -1 * H[t]

def printCodewords(H_n):
	C = []
	H_n[H_n == -1] = 0
	for c in H_n:
		C.append(np.array2string(c))

	H_n[H_n == 0] = -1
	H_n[H_n == 1] = 0
	H_n[H_n == -1] = 1
	for c in H_n:
		C.append(np.array2string(c))
	print(C)

def main():
	n = int(input("Enter value of n in 2^n: "))
	H = generateHadamard(n)
	print(f'Hadamard matrix of order 2^n: \n{H[n]}')
	printCodewords(H[n])

if __name__ == '__main__':
	main()