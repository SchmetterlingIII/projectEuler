'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

squaresList = [(i+1)**2 for i in range(100)]
naturalList = [(i+1) for i in range(100)]


naturals = sum(naturalList)
squareSum = naturals ** 2
sumSquare = sum(squaresList)
output = squareSum - sumSquare

print(output)