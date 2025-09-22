# Start the program

# Step 2: Input
# Read an integer value from the user and take its absolute value
targetNumber = abs(int(input()))

# Step 3: Initialize
index = 0  # Starting index for the calculation

# Step 4: Loop
# Begin an infinite loop
while True:
    # Calculate the sum of the first "index" natural numbers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber
    
    # Step 5: Conditions
    if currentSum == targetNumber:
        # Case when currentSum equals targetNumber
        print(index)  # Print the value of index
        break  # Exit the loop
    elif currentSum > targetNumber:
        # Case when currentSum is greater than targetNumber
        if difference % 2 == 0:
            # Check if the difference is an even number
            print(index)  # Print the value of index
            break  # Exit the loop
    
    # Step 6: Update
    index += 1  # Increment the index by 1

# End of program
