import numpy as np
q = 2
H = np.array([
	[1, 0],
	[1, 1],
	[0, 1],
	[1, 1]
	])
C = np.array([
	[0, 0, 0, 0],
	[1, 1, 1, 0],
	[1, 0, 1, 1],
	[0, 1, 0, 1],
	])

print("The given H is not the parity check matrix as n - k cannot be greater than n but")
print("for transpose of H:")
for c in C:
	p = (c @ H) % q
	print(f'{str(c)}*H = {p}')

print("Hence, transpose of H is a parity check matrix for the given code")