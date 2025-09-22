# Receive Input
targetSum = int(input())  # Get a non-negative integer from the user

# Initialize Variables
currentIndex = 0  # This will track the current integer being processed

# Infinite Loop
while True:
    # Calculate the Sum
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Sum of the first currentIndex integers
    
    # Calculate the Difference
    surplus = currentSum - targetSum  # The surplus amount if currentSum exceeds targetSum

    # Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)  # Output the currentIndex as the solution
        break  # Exit the loop

    # Check for Surplus Condition
    if currentSum > targetSum:
        if surplus % 2 == 0:  # Check if the surplus can be evenly divided by 2
            print(currentIndex)  # Output the currentIndex as the solution
            break  # Exit the loop
    
    # Increment Index
    currentIndex += 1  # Move to the next integer
