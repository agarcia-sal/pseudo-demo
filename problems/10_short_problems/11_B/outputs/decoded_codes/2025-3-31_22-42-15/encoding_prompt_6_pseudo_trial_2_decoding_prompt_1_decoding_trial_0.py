# Step 1: Input
number = abs(int(input()))

# Step 2: Initialize
index = 0

# Step 3: Loop indefinitely
while True:
    # Step 4a: Calculate Triangular Number
    triangularSum = (index * (index + 1)) // 2
    
    # Step 4b: Calculate Difference
    difference = triangularSum - number
    
    # Step 4c: Check Conditions
    if triangularSum == number:
        print(index)  # This indicates that `number` is a triangular number
        break
    elif triangularSum > number:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # This indicates that `number` can be represented as a triangular number with an adjustment
            break
    
    # Step 4d: Increment Counter
    index += 1
