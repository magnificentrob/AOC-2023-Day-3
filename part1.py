file = open('test.txt', 'r')
engine_schematic = []

def checkAdjacency(somelist, x, y):
	print(x,y)

for line in file:
	line = line.strip('\n')
	engine_schematic.append(list(line))
	print(line)

answer = 0

for x in range(len(engine_schematic)):
	for y in range(len(engine_schematic[x])):
		if engine_schematic[x][y].isdigit() == False and engine_schematic[x][y] != '.':
			checkAdjacency(engine_schematic, x, y)
t