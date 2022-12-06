fileName = 'input/day7-test.txt'

lineList = [line.rstrip('\n') for line in open(fileName)]

print(lineList)

all_bags = {}

for line in lineList:
    bag, contents = line.split(' contain ')
    all_bags[bag] = contents

print(all_bags)