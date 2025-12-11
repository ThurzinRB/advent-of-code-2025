import re

def get_input_size(file_path:str):
    with open(file_path, 'r') as mfile:
        for line in mfile:
            line_content = line.rstrip()
            return len(re.split(r' {1,}', line_content))


file_path = 'day6/input/input.txt'
n = get_input_size(file_path)
result_sum = [0]*n
result_mult = [1]*n
result = 0

# print(result_sum)
with open(file_path, 'r') as mfile:
    data = list(map(lambda x: x.strip('\n'), mfile.readlines()))
    numbers = data[:-1]
    operations = re.split(r' {1,}', data[-1])

operation_index = n-1
# for line in numbers:
#     print(line)
sum_results = 0
only_spaces = True
for i in range(len(data[0])-1,-1,-1):
    operation = operations[operation_index]
    print('i: ', i, ' operation: ', operation)
    if only_spaces:
        result=0
        if operation == '*':
            result = 1
    only_spaces = True
    number = ''
    for j, line in enumerate(numbers):
        # print('line[i]: ', line[i])
        if line[i] != ' ':
            only_spaces = False
            number+=line[i]
    if only_spaces:
        print('Result of operation: ', result)
        print('NEXT OPERATION\n\n')
        operation_index-=1
        sum_results+=result
    else:
        # perform operation
        if operation == '*': result*=int(number)
        else: result+=int(number)
        print('number: ', number)
print('Result of operation: ', result)
print('NEXT OPERATION\n\n')
sum_results+=result
    
    
    

print('Result: ', sum_results)