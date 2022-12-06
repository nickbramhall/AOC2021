fileName = 'input/day9-input.txt'

lineList = [line.rstrip('\n') for line in open(fileName)]

print(lineList)

total_cols = len(lineList[0]) + 1
total_rows = len(lineList) + 1

#Surround puzzle grid with 9s

startEnd = '9' * (len(lineList[0])+2)

newLineList = [startEnd]

for line in lineList:
    print(line)
    newline = '9' + line + '9'
    newLineList.append(newline)

newLineList.append(startEnd)

print(newLineList)

def CornerCheck(x,y):
    return 1

def EdgeCheck(x,y):
    return 1

def Check(x,y):
    xy_value = newLineList[x][y]
    print(xy_value)
    above_value = newLineList[x][y-1]
    below_value = newLineList[x][y+1]
    left_value = newLineList[x-1][y]
    right_value = newLineList[x+1][y]
    if xy_value < above_value and xy_value < below_value and xy_value < left_value and xy_value < right_value:
        print('Found low point!')
        return int(xy_value)
    else:
        return False

sum_score=0
row_num=1
for line in newLineList:
    if row_num < total_rows:
        col_num=1
        for char in line:
            if col_num < total_cols:
                print("Checking row {} and column {}".format(row_num,col_num))
                check = Check(row_num,col_num)
                if check is not False:
                    sum_score=sum_score+check+1
                col_num=col_num+1
        row_num=row_num+1

print(sum_score)
