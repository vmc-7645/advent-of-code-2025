
with open('input.txt', 'r') as f:
    lines = [[int(x) for x in line.strip()] for line in f.readlines()]

out = 0

for i in lines:
    max_val = 0
    while i:
        j = i.pop(0)
        test = j if (i==[]) else int(f"{j}{max(i)}")
        if test > max_val: 
            max_val = test
    out += max_val

print(out)

# 17316