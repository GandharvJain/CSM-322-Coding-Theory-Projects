import queue as Q

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
print(huffman_code)