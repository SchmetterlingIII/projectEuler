class problem2:
    B = 1
    A = 0
    total = []

    while True:
        C = B + A
        A = B
        B = C
        
        if C > 4000000:
            break
        total.append(C)
        
    evenTotal = []
    for i in total:
        if i%2 == 0:
            evenTotal.append(i)
   
    finalList = sum(evenTotal)
    print(f'Problem 2: {finalList}')