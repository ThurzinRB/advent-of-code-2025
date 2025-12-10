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
    for line in mfile:
        line_content = line.rstrip().strip(' ')
        print('---------------')
        try:
            items = [int(item) for item in re.split(r' {1,}', line_content)]
            result_mult = [result_mult[i]*items[i] for i in range(n)]
            result_sum = [result_sum[i]+items[i] for i in range(n)]
            print('items:', items)
            print('result_mult:', result_mult)
            print('result_sum:', result_sum)
        except:
            if len(line_content)<n: continue
            operations = re.split(r' {1,}', line_content)
            print(operations)
            for i in range(n):
                if operations[i] == '*':
                    result+=result_mult[i]
                elif operations[i] == '+':
                    result+=result_sum[i]

print('Result: ', result)