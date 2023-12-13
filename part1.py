file = open('test.txt', 'r')

answer = 0

engine_schematic = []
for line in file:
	line = line.strip('\n')
	engine_schematic.append(list(line))

visited = []
for i in range(len(engine_schematic)):
	temp_list = []
	for j in range(len(engine_schematic)):
		temp_list.append('n')
	visited.append(temp_list)

def checkAdjacency(x,y):
	num = ''
	index = 0
	a = x
	b = y
	positions_to_check=[(a-1,b-1), (a-1,b), (a-1,b+1), (a,b+1), (a+1,b+1), (a+1,b), (a+1,b-1), (a,b-1)]
	if x-1 >=0 and y-1 >= 0:
		a = x - 1
		b = y - 1
		if visited[a][b] == 'v':
			return 0
	else:
		return 0
	if engine_schematic[a][b].isdigit() != True:
		return 0
	else:
		for i in range(len(engine_schematic[a][b:]) - 1):
			if engine_schematic[a][index+1].isdigit() == True:
				index +=1
			else:
				break
		for i in reversed(engine_schematic[a][:index+1]):
			if i.isdigit() == True:
				num+=i
			else:
				break
	num = int(num[::-1])
	return num

for i in range(len(engine_schematic)):
	for j in range(len(engine_schematic[i])):
		if engine_schematic[i][j].isdigit() == False and engine_schematic[i][j] != '.':
			answer+=int(checkAdjacency(i,j))
