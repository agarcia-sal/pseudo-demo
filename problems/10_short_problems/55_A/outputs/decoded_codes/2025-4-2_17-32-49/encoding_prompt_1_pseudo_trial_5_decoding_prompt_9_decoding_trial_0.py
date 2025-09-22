# Start the program
n = int(input())  # Input a number n (the maximum size of the list)

# Create a list isAvailable of size n and set all elements to True
isAvailable = [True] * n

# Initialize variables
currentPosition = 0  # This will track the index in isAvailable
incrementValue = 1   # This will be used to determine the current step size

# Set a loop to run while incrementValue is less than or equal to 500,000
while incrementValue <= 500000:
    # If the element at isAvailable[currentPosition] is True
    if isAvailable[currentPosition]:
        # Set isAvailable[currentPosition] to False (mark as unavailable)
        isAvailable[currentPosition] = False
    
    # Increment incrementValue by 1 (move to the next step)
    incrementValue += 1
    
    # Update currentPosition to the new position
    currentPosition = (currentPosition + incrementValue) % n  # Wrap around if it exceeds the size of the list

# Create a new list availablePositions that includes all positions from isAvailable that are still True (available)
availablePositions = [index for index, available in enumerate(isAvailable) if available]

# Check the length of availablePositions
if len(availablePositions) == 0:
    print("YES")  # Output "YES" if all positions were made unavailable
else:
    print("NO")   # Output "NO" if there are still available positions
