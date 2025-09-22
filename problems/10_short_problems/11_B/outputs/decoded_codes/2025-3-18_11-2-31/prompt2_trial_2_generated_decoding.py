# Step 1: Obtain an absolute integer input and assign it to targetNumber
targetNumber = abs(int(input()))

# Step 2: Initialize index to zero
index = 0

# Step 3: Create an infinite loop
while True:
    
    # Step 3a: Calculate the sum of the first index natural numbers
    currentSum = (index * (index + 1)) // 2  # Using the formula for the sum of first n natural numbers
    
    # Step 3b: Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber
    
    # Step 3c: Check if currentSum is equal to targetNumber
    if currentSum == targetNumber:
        print(index)
        break  # Exit the loop if the condition is met
    
    # Step 3d: Check if currentSum is greater than targetNumber
    if currentSum > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop if the condition is met
    
    # Step 3e: Increment index
    index += 1

# Step 4: End of process
