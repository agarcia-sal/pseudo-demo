# Read a non-negative integer from user input
targetSum = abs(int(input()))  # Get and store the absolute value of the input

# Initialize a counter for the index
currentIndex = 0

# Loop indefinitely to find the desired index
while True:
    # Calculate the sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Use integer division
    
    # Calculate the difference between currentSum and targetSum
    difference = currentSum - targetSum
    
    # Check if currentSum is equal to targetSum
    if currentSum == targetSum:
        print(currentIndex)
        break  # Exit the loop
    
    # Check if currentSum is greater than targetSum
    if currentSum > targetSum:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentIndex)
            break  # Exit the loop
    
    # Increment the index for the next iteration
    currentIndex += 1
