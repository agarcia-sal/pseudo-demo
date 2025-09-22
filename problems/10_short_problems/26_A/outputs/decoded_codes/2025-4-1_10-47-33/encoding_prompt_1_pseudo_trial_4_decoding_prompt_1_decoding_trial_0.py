# Step 1: Read an integer value `t` from user input
t = int(input())

# Step 2: Initialize a variable `result` to 0
result = 0

# Step 3: For each integer `i` from 1 to `t` (inclusive)
for i in range(1, t + 1):
    # Initialize a variable `count` to 0
    count = 0
    # Set a variable `currentNumber` equal to `i`
    currentNumber = i
    
    # Step 4: For each integer `j` from 2 to one less than `i`
    for j in range(2, i):
        # If the `currentNumber` is divisible by `j`
        if currentNumber % j == 0:
            # Increment `count` by 1
            count += 1
            # While `currentNumber` is divisible by `j`
            while currentNumber % j == 0:
                # Divide `currentNumber` by `j`
                currentNumber //= j
    
    # Step 5: After checking all possible factors, if `count` is equal to 2
    if count == 2:
        # Increment `result` by 1
        result += 1

# Step 6: After all iterations are done, display the value of `result`
print(result)
