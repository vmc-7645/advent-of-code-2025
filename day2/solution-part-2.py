
# read in input.txt
with open('input.txt', 'r') as f:
    lines = f.read().split(',')

output = 0
for num_range in lines:
    start, end = num_range.split('-')
    for current in range(int(start), int(end) + 1):
        s = str(current)

        # A composit of a string is always going to include said string
        # Thus if composit excludes known repeatability (i.e. ends)
        # Then the tested string in the new string must be a repeated string.
        if s in (s + s)[1:-1]:
            output += current

print(output)