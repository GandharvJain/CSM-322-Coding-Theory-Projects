import numpy as np
q = 2
G = np.array([
	[1, 0, 0, 0, 1],
	[0, 1, 0, 0, 1],
	[0, 0, 1, 1, 1]
	])

print("All the codewords of C are:")
for a_0 in range(q):
	for a_1 in range(q):
		for a_2 in range(q):
			print((G[0] * a_0 + G[1] * a_1 + G[2] * a_2) % q)