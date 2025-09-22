# Start the program
# Input a number n (the maximum size of the list)
n = int(input())

# Create a list isAvailable of size n and set all elements to True
isAvailable = [True] * n

# Initialize currentPosition to 0 and incrementValue to 1
currentPosition = 0
incrementValue = 1

# Set a loop to run while incrementValue is less than or equal to 500,000
while incrementValue <= 500000:
    # If the element at isAvailable[currentPosition] is True
    if isAvailable[currentPosition]:
        # Set isAvailable[currentPosition] to False (mark as unavailable)
        isAvailable[currentPosition] = False
    
    # Increment incrementValue by 1
    incrementValue += 1

    # Update currentPosition
    currentPosition = (currentPosition + incrementValue) % n  # Wrap around if it exceeds the size of the list

# Create a new list availablePositions that includes all positions from isAvailable that are still True
availablePositions = [i for i in isAvailable if i]

# Check the length of availablePositions
if len(availablePositions) == 0:
    # Output "YES" (indicating all positions were made unavailable)
    print("YES")
else:
    # Output "NO" (indicating there are still available positions)
    print("NO")

# End the program
