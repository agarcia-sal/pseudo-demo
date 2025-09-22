# Start the process
targetSum = abs(int(input()))  # Read input and take absolute value
currentIndex = 0  # Initialize a variable to keep track of the current index

# Begin an infinite loop
while True:
    # Calculate the sum of the first 'currentIndex' natural numbers
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Use integer division for sum
    
    # Calculate the difference between the currentSum and targetSum
    difference = currentSum - targetSum
    
    # Check for equality
    if currentSum == targetSum:
        print(currentIndex)  # Output currentIndex as it is a valid solution
        break  # Exit the loop

    # Check if the sum exceeds the target
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if difference is an even number
            print(currentIndex)  # Output currentIndex as it is also a valid solution
            break  # Exit the loop
    
    # Increment the index for the next iteration
    currentIndex += 1
