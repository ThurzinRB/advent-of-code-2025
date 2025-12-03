def add_rotation(current:int, rotation: str):
    direction = 1 if rotation[0] == 'R' else -1
    value = int(rotation[1:])%100
    result = current+direction*value
    if result < 0: result = result+100
    if result > 99: result = result-100
    return result

position = 50
count = 0

with open("day1/input/input.txt", "r") as mfile:
    for line in mfile:
        rotation=line.rstrip()
        print(position, end=' ')
        print(rotation, end=' ')
        position = add_rotation(position, rotation)
        print(position)
        if position==0: count+=1

print("Count: ", count)