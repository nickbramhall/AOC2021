fileName = 'input/day4-test.txt'

lineList = [line.rstrip('\n') for line in open(fileName)]

print(lineList)

choices = lineList[0]

print(choices)

j=0
i=0
board=[]

for line in lineList:
    if line == '':
        board.append([lineList[i+1], lineList[i+2], lineList[i+3], lineList[i+4], lineList[i+5]])
        j = j + 1
    i = i + 1
    print(i)

print(board)