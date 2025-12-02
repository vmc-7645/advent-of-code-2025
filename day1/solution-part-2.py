

# read in input.txt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# starting position
current_pos = 50

# 0 pos count
times_zero = 0

# for each line
while lines:

    # current movement
    current_mvmt = lines.pop(0)
    direction = -1 if current_mvmt[0] == 'L' else 1
    steps = int(current_mvmt[1:])

    if direction == 1:
        times_crossed_zero = (current_pos + steps) // 100 - current_pos // 100
    else:
        times_crossed_zero = (-current_pos + steps) // 100 - (-current_pos) // 100
    
    times_zero += times_crossed_zero
    
    current_pos = (steps * direction + current_pos) % 100

print(times_zero)

# 5829 too high
# 5797 too low