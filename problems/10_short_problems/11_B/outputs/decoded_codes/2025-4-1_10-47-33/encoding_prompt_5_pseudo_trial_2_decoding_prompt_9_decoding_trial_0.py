# Start Program

# Input the Number
targetSum = abs(int(input()))  # Read input and convert it to an absolute integer

# Initialize Counter
index = 0

# Begin Infinite Loop
while True:
    # Calculate the Sum of the First 'index' Integers
    currentSum = (index * (index + 1)) // 2  # Use integer division for sum

    # Calculate the Difference
    difference = currentSum - targetSum  # Determine the difference

    # Check for Equality
    if currentSum == targetSum:
        print(index)  # Output the result
        break  # Exit the loop

    # Check for Exceeding the Target
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output the result
            break  # Exit the loop

    # Increment the Counter
    index += 1  # Increase the value of index by 1

# End Program
