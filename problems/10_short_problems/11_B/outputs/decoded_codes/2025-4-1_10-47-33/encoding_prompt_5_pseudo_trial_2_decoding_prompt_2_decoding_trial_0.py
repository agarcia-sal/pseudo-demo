# Start Program

# Input the Number:
targetSum = abs(int(input()))

# Initialize Counter:
index = 0

# Begin Infinite Loop:
while True:
    # Calculate the Sum of the First 'index' Integers:
    currentSum = (index * (index + 1)) // 2  # Using integer division

    # Calculate the Difference:
    difference = currentSum - targetSum

    # Check for Equality:
    if currentSum == targetSum:
        print(index)  # Print the result
        break  # Exit the loop

    # Check for Exceeding the Target:
    if currentSum > targetSum:
        # Check if difference is even:
        if difference % 2 == 0:
            print(index)  # Print the result
            break  # Exit the loop

    # Increment the Counter:
    index += 1

# End Program
