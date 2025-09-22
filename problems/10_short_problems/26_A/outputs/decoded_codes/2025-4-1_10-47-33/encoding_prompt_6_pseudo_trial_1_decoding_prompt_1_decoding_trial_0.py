# 1. Start the program (implicit in Python execution)
# 2. Read an integer value 't' from the user
t = int(input())

# 3. Initialize a variable 'result' to zero
result = 0

# 4. For each integer 'i' from 1 to 't' (inclusive):
for i in range(1, t + 1):
    # a. Initialize a count variable 'count' to zero
    count = 0
    # b. Set 'currentNumber' to 'i'
    currentNumber = i
    
    # 5. For each integer 'j' from 2 to (i - 1):
    for j in range(2, i):
        # a. Check if 'currentNumber' is divisible by 'j'
        if currentNumber % j == 0:
            # b. If 'currentNumber' is divisible by 'j':
            # i. Increment 'count' by 1
            count += 1
            
            # ii. While 'currentNumber' is divisible by 'j':
            while currentNumber % j == 0:
                # 1. Divide 'currentNumber' by 'j' to remove the factor
                currentNumber //= j
    
    # 6. If 'count' is equal to 2:
    if count == 2:
        # a. Increment 'result' by 1
        result += 1

# 7. Output the value of 'result'
print(result)
# 8. End the program (implicit in Python execution)
