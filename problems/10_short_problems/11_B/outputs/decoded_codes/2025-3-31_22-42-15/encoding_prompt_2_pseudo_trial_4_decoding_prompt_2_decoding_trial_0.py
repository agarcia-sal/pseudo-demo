# Start

# Step 2: Input an integer and take its absolute value
targetNumber = abs(int(input()))

# Step 3: Initialize the index variable
index = 0

# Step 4: Infinite loop
while True:
    # Calculate currentSum
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference
    difference = currentSum - targetNumber
    
    # Step 5: Conditions
    if currentSum == targetNumber:
        print(index)
        break  # Exit the loop
    elif currentSum > targetNumber:
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop
            
    # Step 6: Update the index
    index += 1

# End
