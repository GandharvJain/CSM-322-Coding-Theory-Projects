def parseInput(d):
	codewords = list()
	message, encoding = d.split(',', 1)
	message = message.strip().strip('\'')

	pairs = encoding.strip().strip('{}').split(',')
	for i in pairs:
		pair = i.split(':')
		codewords.append(pair[1].strip().strip('\''))
	return message, codewords


raw_input = input("Enter received word and encoding (Ex - '01', {A: '1', B: '0'}): ")
message, codewords = parseInput(raw_input)
codewords.sort(key = len)

n = len(codewords)
count = 0

# Check if codeword has prefix and increment count if completely decodable
def checkCodewordPrefix(msg):
	global count
	if (len(msg) == 0):
		count = count + 1
		return

	for c in codewords:
		if msg.startswith(c):
			checkCodewordPrefix(msg[len(c):])

checkCodewordPrefix(message)
print(count)