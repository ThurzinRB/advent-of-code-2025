def get_largest_bat(bank:str):
    bigger = 0
    localindex = 0
    for i, bat in enumerate(bank):
        if int(bat)>bigger:
            bigger = int(bat)
            localindex = i
    return [localindex, bigger]

def get_largest_combination(bank: str, num):
    globalindex = 0
    low = 0
    result = ''
    item = 0
    up = -num+1

    for i in range(0, num):
        up = -(num-i)+1
        if up ==0:
            [localindex, item] = get_largest_bat(bank[low:])
        else: 
            [localindex, item] = get_largest_bat(bank[low:up])
        globalindex = localindex+low
        low = globalindex+1
        result+=str(item)


    return result

with open("day3/input/input.txt", 'r') as mfile:
    result = 0
    for line in mfile:
        bank = line.rstrip()
        result+=int(get_largest_combination(bank,12))
    print('sum: ', result)
    