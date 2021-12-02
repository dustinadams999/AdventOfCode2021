import sys

directions = {
    "forward": (lambda curr_x, curr_y, aim, val: (curr_x + val, curr_y + aim*val, aim)),
    "down": (lambda curr_x, curr_y, aim, val: (curr_x, curr_y, aim + val)),
    "up": (lambda curr_x, curr_y, aim, val: (curr_x, curr_y, aim - val))
}

f = open(sys.argv[1], 'r')
lines = [_.replace('\n', '') for _ in f.readlines()]

horizontal_pos = 0
depth = 0
aim = 0

for line in lines:
    action = line.split()[0]
    val = int(line.split()[1])
    horizontal_pos, depth, aim = directions[action](horizontal_pos, depth, aim, val)

print(horizontal_pos*depth)