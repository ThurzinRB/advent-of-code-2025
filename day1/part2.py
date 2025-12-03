def add_rotation(current:int, rotation: str):
    direction = 1 if rotation[0] == 'R' else -1
    value = int(rotation[1:])
    clicks = value//100
    value = value%100
    result = current+direction*value
    if result < 0: 
        result = result+100
        if current!=0 and result !=0:
            clicks+=1
    if result > 99: 
        result = result-100
        if current!=0 and result !=0:
            clicks+=1
    return [result, clicks]

position = 50
count = 0
total_clicks = 0

with open("day1/input/input.txt", "r") as mfile:
    for line in mfile:
        rotation=line.rstrip()
        print('pos: ', position, end='\t')
        print('rot: ',rotation, end='\t')
        [position, clicks] = add_rotation(position, rotation)
        print('clicks: ', clicks, end='\t')
        total_clicks+=clicks
        print('res: ',  position)
        if position==0: count+=1

print("Count: ", count)
print("Clicks: ", total_clicks)
print("Result: ", count+total_clicks)