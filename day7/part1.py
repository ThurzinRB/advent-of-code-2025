file_path = 'day7/input/input.txt'
with open(file_path, 'r') as mfile:
    data = list(map(lambda x: x.strip('\n'),mfile.readlines()))


# print(*data, sep='\n')
initial_beam = data[0].find('S')
split_count = 0 
current = [False]*len(data[0])
next = [False]*len(data[0])

current[initial_beam] = True
print(initial_beam)

for i in range(len(data)-1):
    print('--------')
    print(current)
    for j in range(len(data[i])):
        if current[j]:
            if data[i+1][j] == '^':
                split_count+=1
                next[j] = False
                next[j+1] = True
                next[j-1] = True
            else:
                next[j] = True
            
    current=next
print(split_count)