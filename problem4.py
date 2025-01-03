number = 102941
is_palindrome = True 
numberList = [int(i) for i in str(number)]
leng = len(numberList)

print(f"Number List: {numberList}")  # Debugging: Show the numberList

for i in range(leng // 2):
    print(f"Comparing {numberList[i]} and {numberList[leng - i - 1]}")  # Debugging
    if numberList[i] != numberList[leng - i - 1]:
        is_palindrome = False
        print("Mismatch found. Breaking loop.")  # Debugging
        break

if is_palindrome:
    print("The number is a palindrome")
else:
    print("Not a palindrome")