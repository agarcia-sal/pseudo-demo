# Program to find the triangular number corresponding to the user input

# Step 1: Input the integer from the user and convert to its absolute value
number = abs(int(input()))

# Step 2: Initialize the counter variable
index = 0

# Step 3: Loop indefinitely until conditions are met
while True:
    # Step 3a: Calculate the Triangular Number using the formula
    triangularSum = (index * (index + 1)) // 2  # Using integer division for accuracy
    
    # Step 3b: Calculate the difference from the input number
    difference = triangularSum - number
    
    # Step 3c: Check conditions for triangular number
    if triangularSum == number:
        # The input number is a triangular number
        print(index)
        break
    elif triangularSum > number:
        # Check if the difference is even
        if difference % 2 == 0:
            # The number can be represented as a triangular number with an adjustment
            print(index)
            break
            
    # Step 3d: Increment the counter
    index += 1
