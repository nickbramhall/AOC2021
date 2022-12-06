import string

fileName = 'input/day6-input.txt'

lineList = [line.rstrip('\n') for line in open(fileName)]

print(lineList)

# Combine all answers into one string

entries = []
entry_counter = 0

entries.append('')

for line in lineList:
    if line == '':
        entry_counter += 1
        entries.append('')
    entries[entry_counter] += line

print(entries)

# Test that string against the alphabet

all_alphabet = list(string.ascii_lowercase)

print(all_alphabet)

total_score = 0

for entry in entries:
    entry_score = 0
    for c in all_alphabet:
        if c in entry:
            entry_score += 1
    total_score = total_score + entry_score

print(total_score)