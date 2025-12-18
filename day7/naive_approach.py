import copy

class TimeLine:
    def __init__(self, path:list):
        self.path = path
    def addNode(self, node: int):
        node_copy = copy.deepcopy(node)
        self.path.append(node_copy)
    def __str__(self):
        timeLinestring = ', '.join(list(map(str, self.path)))
        return timeLinestring

file_path = 'day7/input/input.txt'
with open(file_path, 'r') as mfile:
    data = list(map(lambda x: x.strip('\n'),mfile.readlines()))


# print(*data, sep='\n')
current_timeLines = []
initial_beam = data[0].find('S')
split_count = 0 
current = [False]*len(data[0])
next = [False]*len(data[0])

current[initial_beam] = True
current_timeLines.append(TimeLine([initial_beam]))
# print(*current_timeLines, sep= ' | ')
next_timeLines = []




for i in range(len(data)-1):
    print('\n\nline:', i)
    # print(*current_timeLines, sep= ' \n')

    for timeLine in current_timeLines:
        current_node = timeLine.path[-1]
        if data[i+1][current_node] == '^':

            # print('found ^ splitting')

            left_timeLine = copy.deepcopy(timeLine)
            left_timeLine.addNode(current_node-1)
            right_timeLine = copy.deepcopy(timeLine)
            right_timeLine.addNode(current_node+1)
            
            next_timeLines.append(left_timeLine)
            next_timeLines.append(right_timeLine)
            
        else:
            # print('going straight to: ', current_node)
            straight_timeLine = copy.deepcopy(timeLine)
            straight_timeLine.addNode(current_node)
            next_timeLines.append(straight_timeLine)
        # print('---next_timelines---')
        # print(*next_timeLines, sep= ' \n')
    current_timeLines = next_timeLines
    next_timeLines = []




    # for j in range(len(data[i])):
    #     if current[j]:
    #         if data[i+1][j] == '^':
    #             split_count+=1
    #             next[j] = False
    #             next[j+1] = True
    #             next[j-1] = True
    #         else:
    #             next[j] = True
            
    # current=next
# print('\n\n\nTimeline result')
# print(*current_timeLines, sep= ' \n')
print('Result: ', len(current_timeLines))
