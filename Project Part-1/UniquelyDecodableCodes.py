def parseInput(d):
	codewords = list()
	message, encoding = d.split(',', 1)
	message = message.strip().strip('\'')
	pairs = encoding.strip().strip('{}').split(',')
	for i in pairs: codewords.append(i.split(':')[1].strip().strip('\''))
	return message, codewords

message, codewords = parseInput(input("Enter received word and encoding (Ex - '01', {A: '1', B: '0'}): "))
count = 0
def checkCodewordPrefix(msg):
	global count
	if (len(msg) == 0):
		count = count + 1
		return
	for c in codewords:
		if msg.startswith(c): checkCodewordPrefix(msg[len(c):])

checkCodewordPrefix(message)
print(count)