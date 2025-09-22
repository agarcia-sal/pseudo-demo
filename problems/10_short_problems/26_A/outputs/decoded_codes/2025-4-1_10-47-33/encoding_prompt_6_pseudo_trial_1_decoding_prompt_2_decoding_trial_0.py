# Start the program
# Step 2: Read an integer value 't' from the user
t = int(input())

# Step 3: Initialize a variable 'result' to zero
result = 0

# Step 4: For each integer 'i' from 1 to 't' (inclusive):
for i in range(1, t + 1):
    # Step 4a: Initialize a count variable 'count' to zero
    count = 0
    # Step 4b: Set 'currentNumber' to 'i'
    currentNumber = i
    
    # Step 5: For each integer 'j' from 2 to (i - 1):
    for j in range(2, i):
        # Step 5a: Check if 'currentNumber' is divisible by 'j'
        if currentNumber % j == 0:
            # Step 5b: If 'currentNumber' is divisible by 'j':
            # Step 5bi: Increment 'count' by 1
            count += 1
            
            # Step 5bii: While 'currentNumber' is divisible by 'j':
            while currentNumber % j == 0:
                # Step 5bii1: Divide 'currentNumber' by 'j' to remove the factor
                currentNumber //= j
    
    # Step 6: If 'count' is equal to 2:
    if count == 2:
        # Step 6a: Increment 'result' by 1
        result += 1

# Step 7: Output the value of 'result'
print(result)

# Step 8: End the program
