class problem3Inefficient:
    intInput = int(input("Enter an integer, smaller than 1000: "))
    seed = 2
    store = []
    primeFactor = []
    for i in range(intInput-1):
        if intInput%seed == 0:
            primeFactor.append(seed)
        store.append(seed)
        seed += 1
        for i in store:
            if seed%i == 0:
                store.remove(i)

    primeFactor.remove(intInput)
    print(f'Problem 3: {max(primeFactor)}')

class problem3Improved:
    factor = 2
    n = int(input('Enter any integer: '))
    # largest prime cannot be larger than the sqrt(input)
    while factor ** 2 <= n:
        if n%factor == 0:
            n //= factor
        else:
            factor += 1
    print(f'Problem 3 (improved): {factor}')