# Step 1: Read an integer value `t` from input.
t = int(input())

# Step 2: Initialize a variable `result` to 0.
result = 0

# Step 3: For each integer `i` from 1 to `t` (inclusive):
for i in range(1, t + 1):
    # Initialize `count` to 0 for the current integer `i`.
    count = 0
    number = i

    # Step 4: For each integer `j` from 2 to `i-1` (inclusive):
    for j in range(2, i):
        # Check if `number` is divisible by `j`:
        if number % j == 0:
            # If true, increase `count` by 1.
            count += 1
            
            # Keep dividing `number` by `j` until `number` is no longer divisible by `j`.
            while number % j == 0:
                number //= j
                
    # Step 5: After checking all potential factors:
    # If `count` is equal to 2:
    if count == 2:
        # Increase `result` by 1.
        result += 1

# Step 6: Output the value of `result`.
print(result)
