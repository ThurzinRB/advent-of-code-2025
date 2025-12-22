def get_area(A, B):
    dx = abs(A[0] - B[0])+1
    dy = abs(A[1] - B[1]) + 1

    return dx*dy
data = []
with open('day9/input/input.txt') as mfile:
    for line in mfile:
        strip_line = line.rstrip()
        data.append(list(map(int,strip_line.split(','))))

print(data)
biggest = 0


for i in range(len(data)):
    for j in range(i,len(data)):
        A = get_area(data[i], data[j])
        if A>biggest: biggest = A
        print(data[i], data[j], end = '\t')
        print(A)

print("Result: ", biggest)