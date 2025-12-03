def add_rotation(current:int, rotation: str):
    '''Calculates the result given its current position\n
    current (int): current position\n
    rotation (str): rotation (L30 for example)\n
    returns [result, clicks] (int, int): result of a rotation and number of clicks during the rotation\n
    '''

    # the direction is the sign of the rotation operation
    direction = 1 if rotation[0] == 'R' else -1
    value = int(rotation[1:])

    # the number of clicks will be the number of full revolutions of a rotation + the click if the last rotation passes the 0
    # here I calculate the number of full rotations
    clicks = value//100

    # after the calculation, remove the rotation from the value
    # this means get the module operation
    value = value%100

    # the result will the sum of current position and the value using the direction as the sign of value
    result = current+direction*value

    # if the result is -12, for example we need to add 100 so the actual answer is 88
    # this also means that we have to add 1 to the count of clicks of that rotation
    # I just don't add 1 to the clicks count if the result is 0 bc I already account for this outside the function
    if result < 0: 
        result = result+100
        if current!=0 and result !=0:
            clicks+=1

    # do the same if the value is 112 for example
    if result > 99: 
        result = result-100
        if current!=0 and result !=0:
            clicks+=1
    return [result, clicks]



# initial values
position = 50
count = 0
total_clicks = 0

with open("day1/input/input.txt", "r") as mfile:
    

    for line in mfile:
        # each rotation calculate the result
        # sum the number of clicks on the total_clicks count
        # sum if it points to 0 to count
        rotation=line.rstrip()
        print('pos: ', position, end='\t')
        print('rot: ',rotation, end='\t')
        [position, clicks] = add_rotation(position, rotation)
        print('clicks: ', clicks, end='\t')
        total_clicks+=clicks
        print('res: ',  position)
        if position==0: count+=1


# the result will be the sum of total clicks and count
print("Count: ", count)
print("Clicks: ", total_clicks)
print("Result: ", count+total_clicks)