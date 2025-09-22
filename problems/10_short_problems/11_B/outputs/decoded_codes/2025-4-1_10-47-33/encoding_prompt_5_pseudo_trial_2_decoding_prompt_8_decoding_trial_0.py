# Start Program

# Input the Number
targetSum = abs(int(input()))

# Initialize Counter
index = 0

# Begin Infinite Loop
while True:
    # Calculate the Sum of the First 'index' Integers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the Difference
    difference = currentSum - targetSum
    
    # Check for Equality
    if currentSum == targetSum:
        print(index)  # Print the result we are looking for
        break  # Exit the loop
        
    # Check for Exceeding the Target
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the valid result
            break  # Exit the loop

    # Increment the Counter
    index += 1

# End Program
