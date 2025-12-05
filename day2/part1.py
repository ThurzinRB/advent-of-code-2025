def get_invalid_ids(lower:str, upper:str):
    n_digit_lower = len(lower)
    n_digit_upper = len(upper)

    result = []

    for n in range(n_digit_lower, n_digit_upper+1):
        print('--------')
        print(n)
        if n%2==0:
            ranged = 10**(n//2-1)
            if n_digit_lower%2==0 and ranged < int(lower[:n_digit_lower//2]):
                ranged = int(lower[:n_digit_lower//2])
            rangeu = 10**(n//2)
            if n_digit_upper%2==0 and rangeu > int(upper[:n_digit_upper//2]):
                rangeu = int(upper[:n_digit_upper//2])+1
            print('ranged: ', ranged)
            print('rangeu: ', rangeu)
            l = [int(str(i)+str(i)) for i in list(range(ranged,rangeu))]
            if len(l)>=1:
                if l[0]<int(lower): l.pop(0)
                if l[-1]> int(upper): l.pop(-1)
            result = result + l
    return result


                
                

# print(get_invalid_ids('38593856','38593862'))
# print(get_invalid_ids('1000','8000'))
print(get_invalid_ids('22951285','23017127'))
# 22951285-23017127


result = 0

with open("day2/input/input.txt", "r") as mfile:
    content = mfile.read()
    intervals = content.split(',')
    intervals = [intervals[-1]]
    for interval in intervals:
        [lower, upper] = [int(x) for x in interval.split('-')]
        [lower, upper] = interval.split('-')
        invalid = get_invalid_ids(lower, upper)
        print('inv: ', invalid, end='')
        print('int: ', interval, end=' ')
        print('low: ', lower, end=' ')
        print('up: ', upper, end=' ')
        result+=sum(invalid)
        print()
    print('Result: ', result)