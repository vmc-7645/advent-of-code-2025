
# I hate this solution, super inefficient
with open('input.txt', 'r') as f:
    lines = [[int(x) for x in line.strip()] for line in f.readlines()]

out = 0

def fct(start, placement, values):
    if placement == 0: return ""
    n = len(values)
    last_idx = n - placement
    if start > last_idx: return None
    rng = values[start:last_idx + 1]
    if not rng: return None
    mx = max(rng)
    right = fct(rng.index(mx) + start + 1, placement - 1, values)
    if right is None: return None
    return f"{mx}{right}"

for i in lines:
    max_val = 0
    while i:
        j = i.pop(0)
        tail = fct(0, 11, i)
        if tail is None: continue
        test = int(f"{j}{tail}")
        if test > max_val: max_val = test
    out += max_val

print(out)
# 171741365473332