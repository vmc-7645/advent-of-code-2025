
with open('input.txt', 'r') as f:
    lines = [list(line) for line in f.read().split('\n')]
out = 0
changed = True
while changed:
    to_test = [row[:] for row in lines]
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
                to_test[y][x] = '.'
    if to_test == lines:
        changed = False
    lines = to_test
print(out)
# 8442