import copy

file_path = 'day7/input/input.txt'

class Spot():
    def __init__(self, value:bool = False, count: int = 0):
        self.value = value
        self.count = count
    def set_value(self, value:bool = False):
        self.value = value
        if value == False: self.count=0
    def add_count(self, count):
        self.count+=count
    def set_count(self, count):
        self.count=count
    def __str__(self):
        return str(self.value) + ' ' + str(self.count)


with open(file_path, 'r') as mfile:
    data = list(map(lambda x: x.strip('\n'),mfile.readlines()))


# print(*data, sep='\n')
initial_beam = data[0].find('S')
split_count = 0
current = [Spot() for i in range(len(data)-1)]
next = [Spot() for i in range(len(data)-1)]

current[initial_beam] = Spot(True, 1)
# print(initial_beam)
# print(data[2][7])

for i in range(len(data)-1):
    # print('--------')
    # print(*list(data[i]), sep=' ')
    # print(*current, sep=', ')
    next = [Spot() for i in range(len(data)-1)]
    for j in range(len(data[i])):
        # print('\n\ni: ',i, 'j: ', j)
        if current[j].value:
            # print('current[j].value==True')
            # print(data[i+1][j])
            if data[i+1][j] == '.':
                # print('data[i+1][j] != \'^\'')
                # next[j] = Spot(True, 1)
                next[j].set_value(True)
                next[j].add_count(current[j].count)
                # next[j].se(current[j].count)
                # print(*next, sep=', ')
            else:
                # print('data[i+1][j] == \'^\'')
                # print('current[j]', current[j])
                split_count+=1
                next[j].set_value(False)
                next[j+1].set_value(True)
                next[j+1].add_count(current[j].count)
                next[j-1].set_value(True)
                next[j-1].add_count(current[j].count)

    # print(*next, sep=', ')
            
    print(*[spot.count if spot.count>0 else data[i][k] for k, spot in enumerate(current)])
    current=copy.deepcopy(next)
print(*current)
result = sum([i.count for i in current])
print(split_count)
print(result)