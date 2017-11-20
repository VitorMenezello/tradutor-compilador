import sys

def isLabel(token):
	if (len(token) > 1):
		if (token[0] == 'L'):
			return True
	return False

def isOp(line, i):
	if (len(line) - i == 3):
		return True

def isLogic(token):
	if (token == "if" or token == "iffalse"):
		return True
	return False

def isGoto(token):
	if (token == "goto"):
		return True
	return False

def buildQuadruple(op, res, arg1 = None, arg2 = None):
	quad = {}
	quad['res'] = res
	quad['arg1'] = arg1
	quad['arg2'] = arg2
	quad['op'] = op
	return quad


# Main
fileName = sys.argv[1]

with open(fileName) as f:
    content = f.readlines()

content = [l.strip() for l in content]
content = [l.replace(':',' ') for l in content]

labels = {}
symbols = []
quads = []
address = 0
temp = 1

for l in content:
	line = l.split()
	i = 0
	while (i < len(line) and isLabel(line[i])):
		labels[line[i]] = address
		i += 1
	if (i < len(line)):
		if (isLogic(line[i])):
			tempVar = 'temp' + str(temp)
			symbols.append(tempVar)
			temp += 1

			quad = buildQuadruple(line[i + 2], tempVar, line[i + 1], line[i + 3])
			quads.append(quad)

			quad = buildQuadruple(line[i], line[i + 5], tempVar)
			quads.append(quad)

		elif (isGoto(line[i])):
			quad = buildQuadruple(line[i], line[i + 1])
			quads.append(quad)

		elif (isOp(line, i)):
			quad = buildQuadruple(line[i + 1], line[i], line[i + 2])
			quads.append(quad)

		else:
			quad = buildQuadruple(line[i + 3], line[i], line[i + 2], line[i + 4])
			quads.append(quad)

	address += 1

for q in quads:
 	print q