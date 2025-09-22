# Step 1: Read an integer value t from user input
t = int(input())

# Step 2: Initialize result to 0
result = 0

# Step 3: Loop through each integer i from 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize count to 0 for counting distinct prime factors
    count = 0
    # Set currentNumber equal to i
    currentNumber = i
    
    # Step 4: Loop through each integer j from 2 to i-1
    for j in range(2, i):
        # Check if currentNumber is divisible by j
        if currentNumber % j == 0:
            # Increment count by 1 for a new prime factor
            count += 1
            # While currentNumber is divisible by j, divide it
            while currentNumber % j == 0:
                currentNumber //= j  # Remove all occurrences of factor j

    # Step 5: Check if count is exactly 2
    if count == 2:
        # Increment result since i has exactly two distinct prime factors
        result += 1

# Step 6: Display the value of result
print(result)
