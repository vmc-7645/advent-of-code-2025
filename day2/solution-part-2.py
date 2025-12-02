
# read in input.txt
with open('input.txt', 'r') as f:
    lines = f.read().split(',')

output = 0
for num_range in lines:
    start, end = num_range.split('-')
    for current in range(int(start), int(end) + 1):
        s = str(current)

        # A composit of a base string is always going to include the base string
        # Thus if the composit excludes known repeatability (i.e. ends)
        # Then the base string in the new string must be a repeated string.
        # If base string is not found it mean no repeatability is in the composit
        if s in (s + s)[1:-1]:
            output += current

print(output)