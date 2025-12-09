def parse_input(file_path:str):
    with open(file_path, 'r') as mfile:
        is_interval = True
        intervals = []
        ids = []
        for line in mfile:
            line_content = line.rstrip()
            if len(line_content) == 0: 
                is_interval=False
                continue
            if is_interval:
                [low, up] = line_content.split('-')
                intervals.append([int(low),int(up)])
            else:
                ids.append(int(line_content))
        return [intervals, ids]
        
[intervals, ids] = parse_input('day5/input/input.txt')
print('intervals: ', intervals)
print('ids: ', ids)

result = 0
for id in ids:
    for interval in intervals:
        if id>=interval[0] and id<=interval[1]:
            result+=1
            break
print('Result: ', result)