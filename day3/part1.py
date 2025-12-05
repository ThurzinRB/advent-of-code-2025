def get_largest_bat(bank:str):
    bigger = 0
    index = 0
    for i, bat in enumerate(bank):
        if int(bat)>bigger:
            bigger = int(bat)
            index = i
    return [index, bigger]

def get_largest_pair(bank: str):
    print(bank, end=' ')
    [index_first, first] = get_largest_bat(bank[:-1])
    print(f'[{index_first}, {first}]', end=' ')
    [index_second, second] = get_largest_bat(bank[index_first+1:])
    # print(bank[index_first+1:], end=' ')
    print(f'[{index_second}, {second}]', end=' ')
    result = str(first)+str(second)
    print('result: ', result, end=' ')
    print()
    
    return result

with open("day3/input/input.txt", 'r') as mfile:
    result = 0
    for line in mfile:
        bank = line.rstrip()
        result+=int(get_largest_pair(bank))
    print('sum: ', result)
    