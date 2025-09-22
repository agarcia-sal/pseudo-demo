# Step 1: Input from user
number = abs(int(input()))

# Step 2: Initialize counter variable
index = 0

# Step 3: Loop indefinitely
while True:
    # Step 3a: Calculate Triangular Number
    triangularSum = (index * (index + 1)) // 2  # Using integer division

    # Step 3b: Calculate Difference
    difference = triangularSum - number

    # Step 3c: Check Conditions
    if triangularSum == number:
        print(index)  # number is a triangular number
        break
    elif triangularSum > number:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # number can be represented as a triangular number with an adjustment
            break

    # Step 3d: Increment Counter
    index += 1
