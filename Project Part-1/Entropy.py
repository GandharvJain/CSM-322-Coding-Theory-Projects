import queue as Q
from math import log

def parseInput(d):
	source = dict()
	pairs = d.strip().strip('{}').split(',')
	for i in pairs:
		pair = i.split(':')
		source[pair[0].strip().strip('\'')] = int(pair[1].strip().strip('\''))
	return source

class node:
	def __init__(self, freq, symbol, left=None, right=None):
		self.freq = freq
		self.symbol = symbol
		self.left = left
		self.right = right

	def __lt__(self, other):
		return self.freq < other.freq

def assignCodes(node, code=''):
	global huffman_code

	if not node.left and not node.right:
		huffman_code[node.symbol] = code
	else:
		if node.left:
			assignCodes(node.left, code + '0')
		if node.right:
			assignCodes(node.right, code + '1')

raw_input = input("Enter symbols and frequencies (Ex - {A: 12, B: 5}): ")
source = parseInput(raw_input)

n = len(source)
f_total = sum(source.values())

pq = Q.PriorityQueue()
huffman_code = dict()

for alphabet, frequency in source.items():
	pq.put(node(frequency, alphabet))

while pq.qsize() > 1:
	left = pq.get()
	right = pq.get()

	new_node = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
	pq.put(new_node)

assignCodes(pq.get())

for k in source:
	source[k] /= f_total

huffman_avg_word_len = sum(len(v) * source[k] for k, v in huffman_code.items())

print(source.values())
source_entropy = sum(-1 * p * log(p, 2) for p in source.values())

print(f"Entropy of Huffman code: {huffman_avg_word_len}")
print(f"Entropy of optimal structure: {source_entropy}")