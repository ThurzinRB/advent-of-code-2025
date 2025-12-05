def is_invalid(value: int):
    value_str = str(value)
    for i in range(1,len(str(value))//2+1):
        copy = value_str
        while copy[:i] == copy[i:2*i]:
            copy = copy[i:]
            if len(copy[i:2*i])==0:
                return True

    return False

def get_invalid_ids(lower:str, upper:str):
    result = []
    for x in range(int(lower),int(upper)+1):
        is_inv = is_invalid(x)
        if is_inv:
            result.append(x)

    return result


                
                




result = 0

with open("day2/input/input.txt", "r") as mfile:
    content = mfile.read()
    intervals = content.split(',')
    for interval in intervals:
        [lower, upper] = [int(x) for x in interval.split('-')]
        [lower, upper] = interval.split('-')
        invalid = get_invalid_ids(str(int(lower)), str(int(upper)))
        print('inv: ', invalid, end=' ')
        print('int: ', interval, end=' ')
        print('up: ', str(int(upper)), end=' ')
        result+=sum(invalid)
        print()
    print('Result: ', result)