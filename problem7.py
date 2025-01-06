def wholeNumCheck(x):
    return x / 1 == int(x)  # Checks if x is a whole number, although has become redundant here

def main():
    primes = [2, 3, 5, 7, 11, 13]  # Initial list of primes

    for no in range(14, 1000000):  # Check numbers between 14 and some arbitrarily large number
        is_prime = True 
        for i in primes:
            if i * i > no:  # Optimization: Stop checking if `i` exceeds sqrt(no)
                break
            if no % i == 0:  # If divisible by a prime, it's not a prime
                is_prime = False
                break
        if is_prime:  # Append only if the number is prime
            primes.append(no)

    print(primes[10000])  # Print the number in the 10001st position

# Run the main function
main()