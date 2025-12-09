def parse_grid(file_path:str):
    result = []
    with open(file_path, "r") as mfile:
        for line in mfile:
            line_string = line.rstrip()
            result.append(list(line_string))
    return result

def pretty_print(matrix: list):
    for line in matrix:
        print(' '.join(line))


def get_neighbours(i:int, j:int, matrix):
    result = []
    n = len(matrix)
    m = len(matrix[0])
    min_i = max(i-1, 0)
    min_j = max(j-1, 0)
    max_i = min(n-1,i+1)
    max_j = min(m-1,j+1)

    # print('i: ', i)
    # print('j: ', j)
    # print('min_i: ', min_i)
    # print('min_j: ', min_j)
    # print('max_i: ', max_i)
    # print('max_j: ', max_j)
    count = 0

    for ci in range(min_i,max_i+1):
        for cj in range(min_j, max_j+1):
            if ci==i and cj==j:
                pass
            else:
                count+=matrix[ci][cj] == '@'

    return count



matrix = parse_grid("day4/input/input.txt")
print(matrix)
print('\n\n')
pretty_print(matrix)

result = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        number = get_neighbours(i,j,matrix)
        char = '-'
        if number<4 and matrix[i][j] == '@': 
            char='<'
            result+=1
        print(matrix[i][j],char,number, end='\t')
    print('')
print('Result: ', result)