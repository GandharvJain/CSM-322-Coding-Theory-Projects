import queue as Q
from math import log

def parseInput(d):
	source = dict()
	pairs = d.strip().strip('{}').split(',')
	for i in pairs:
		pair = i.split(':')
		source[pair[0].strip().strip('\'')] = float(pair[1].strip().strip('\''))
	return source

class node:
	def __init__(self, frq, sym, left=None, right=None):
		self.frq = frq
		self.sym = sym
		self.left = left
		self.right = right
	def __lt__(self, other): return self.frq < other.frq

def assignCodes(node, code=''):
	global huffman_code
	if not node.left and not node.right: huffman_code[node.sym] = code
	if node.left: assignCodes(node.left, code + '0')
	if node.right: assignCodes(node.right, code + '1')

source = parseInput(input("Enter symbols and frequencies (Ex - {A: 12, B: 5}): "))
pq = Q.PriorityQueue()
huffman_code = dict()

for alphabet, frequency in source.items(): pq.put(node(frequency, alphabet))
while pq.qsize() > 1:
	left = pq.get()
	right = pq.get()
	pq.put(node(left.frq + right.frq, left.sym + right.sym, left, right))
assignCodes(pq.get())

f_total = sum(source.values())
for k in source: source[k] /= f_total
huffman_avg_word_len = sum(len(v) * source[k] for k, v in huffman_code.items())
source_entropy = sum(-1 * p * log(p, 2) for p in source.values())

print(f"Entropy of Huffman code: {round(huffman_avg_word_len, 8)}")
print(f"Entropy of optimal structure: {round(source_entropy, 8)}")