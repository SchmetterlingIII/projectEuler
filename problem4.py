'''Find the largest palindrome made from the product of two 3-digit numbers.'''

'''Finding products of the largest 3-digit numbers'''
def corr():
    input1 = 999
    input2 = 999
    correct = True
    while correct:
        number = input1 * input2
        if not is_palindrome(number):
            if input2 > 899: 
                input2 -= 1
            else: 
                input1 -= 1
                input2 = 999
        else:
            correct = False
            break
    print(f'The largest palindrome is: {number}, from {input1} * {input2}')
  
'''Verifying whether a number is a palindrome'''
def is_palindrome(number):
    numberList = [int(i) for i in str(number)]
    leng = len(numberList)
    for i in range(leng // 2):
        if numberList[i] != numberList[leng - i - 1]:
            return False
    return True