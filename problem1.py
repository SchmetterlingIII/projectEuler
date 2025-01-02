class problem1:
    maxNum = 1000
    num = 0
    for integer in range(int(maxNum)):
        if integer%3 == 0 or integer%5 == 0:
            num += integer
    print(f'Problem 1: {num}')