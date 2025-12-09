def parse_input(file_path:str):
    with open(file_path, 'r') as mfile:
        is_interval = True
        intervals = []
        ids = []
        for line in mfile:
            line_content = line.rstrip()
            if len(line_content) == 0: 
                is_interval=False
                break
            [low, up] = line_content.split('-')
            intervals.append([int(low),int(up)])
        return intervals
        
intervals = parse_input('day5/input/basic.txt')
print('intervals: ', intervals)