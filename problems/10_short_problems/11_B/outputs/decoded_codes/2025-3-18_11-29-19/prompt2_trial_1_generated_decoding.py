# Step 1: Define an input variable to store the absolute value of an integer
absoluteInput = abs(int(input()))

# Step 2: Initialize a variable index to zero
index = 0

# Step 3: Enter an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    sumIndex = index * (index + 1) // 2  # Using the formula n(n+1)/2 to get sum of the first n natural numbers
    
    # Compute the difference
    difference = sumIndex - absoluteInput
    
    # Step 4: Check if sumIndex is equal to absoluteInput
    if sumIndex == absoluteInput:
        print(index)  # Output the index as a valid result
        break  # Exit the loop
    
    # Step 5: Check if sumIndex is greater than absoluteInput
    if sumIndex > absoluteInput:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index as a valid result
            break  # Exit the loop
    
    # Step 6: Increment the value of index
    index += 1
