fileName = 'input/day9-input.txt'

lineList = [line.rstrip('\n') for line in open(fileName)]

# print(lineList)

total_cols = len(lineList[0]) + 1
total_rows = len(lineList) + 1

#Surround puzzle grid with 9s

startEnd = '9' * (len(lineList[0])+2)

newLineList = [startEnd]

for line in lineList:
    # print(line)
    newline = '9' + line + '9'
    newLineList.append(newline)

newLineList.append(startEnd)

# print(newLineList)

def CornerCheck(x,y):
    return 1

def EdgeCheck(x,y):
    return 1

def Check(x,y):
    xy_value = newLineList[x][y]
    # print(xy_value)
    above_value = newLineList[x][y-1]
    below_value = newLineList[x][y+1]
    left_value = newLineList[x-1][y]
    right_value = newLineList[x+1][y]
    if xy_value < above_value and xy_value < below_value and xy_value < left_value and xy_value < right_value:
        # print('Found low point!')
        return int(xy_value)
    else:
        return False

low_points = []
sum_score=0
row_num=1
for line in newLineList:
    if row_num < total_rows:
        col_num=1
        for char in line:
            if col_num < total_cols:
                # print("Checking row {} and column {}".format(row_num,col_num))
                check = Check(row_num,col_num)
                if check is not False:
                    sum_score=sum_score+check+1
                    low_points.append((row_num,col_num))
                col_num=col_num+1
        row_num=row_num+1

print(f'Part 1: {sum_score}')
# print(low_points)

# Part 2 - Basins
 
# up:start_row-1,start_col
# down:start_row+1,start_col
# left:start_row,start_col-1
# right:start_row,start_col+1

basins=[]

for point in low_points:

    # print(point)

    checked=[]
    to_check=[point]
    count=1

    all_done=False

    while all_done is False:
        start_row=to_check[0][0]
        start_col=to_check[0][1]
        # print(f'Now checking: {start_row},{start_col}')
        if newLineList[start_row-1][start_col] != '9':
            # print(f'Is {start_row-1},{start_col} in {checked}')
            if (start_row-1,start_col) not in checked:
                if (start_row-1,start_col) not in to_check:
                    count = count + 1
                    to_check.append((start_row-1,start_col))
        if newLineList[start_row][start_col+1] != '9':
            # print(f'Is {start_row},{start_col+1} in {checked}')
            if (start_row,start_col+1) not in checked:
                if (start_row,start_col+1) not in to_check:
                    count = count + 1
                    to_check.append((start_row,start_col+1))
        if newLineList[start_row+1][start_col] != '9':
            # print(f'Is {start_row+1},{start_col} in {checked}')
            if (start_row+1,start_col) not in checked:
                if (start_row+1,start_col) not in to_check:
                    count = count + 1
                    to_check.append((start_row+1,start_col))
        if newLineList[start_row][start_col-1] != '9':
            # print(f'Is {start_row},{start_col-1} in {checked}')
            if (start_row,start_col-1) not in checked:
                if (start_row,start_col-1) not in to_check:
                    count = count + 1
                    to_check.append((start_row,start_col-1))
        checked.append((start_row,start_col))
        del to_check[0]
        if not to_check:
            all_done = True
        
        # print(f'Squares still to_check: {to_check}')
        # print(f'Squares checked: {checked}')

    # print(f'Basin size: {count}')
    basins.append(int(count))

# Now sort the basins from largest to smallest and multiply the sizes of the 3 biggest

basins_sorted=sorted(basins, reverse=True)
total=basins_sorted[0]*basins_sorted[1]*basins_sorted[2]

print(f'Part 2: {total}')