# read in input.txt
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

out = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.': continue
        num = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= len(line) or y + j < 0 or y + j >= len(lines):
                    continue
                if lines[y + j][x + i] == '@':
                    num += 1
        if num < 4:
            out += 1

print(out)
# 1553