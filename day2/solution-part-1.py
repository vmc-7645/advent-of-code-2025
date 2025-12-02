
# read in input.txt
with open('input.txt', 'r') as f:
    lines = f.read().split(',')

print(lines)


output = 0
for num_range in lines:
    start, end = num_range.split('-')
    for current in range(int(start), int(end) + 1):

        # check if number is valid
        if len(str(current)) % 2 != 0:
            continue
        mid = len(str(current)) // 2
        if str(current)[:mid] == str(current)[mid:]:
            output += current # if valid add
        

print(output)