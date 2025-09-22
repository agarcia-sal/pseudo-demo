# Start the program

# Input a number n (the maximum size of the list)
n = int(input())

# Create a list isAvailable of size n and set all elements to True
isAvailable = [True] * n

# Initialize two variables: currentPosition and incrementValue
currentPosition = 0
incrementValue = 1

# Set a loop to run while incrementValue is less than or equal to 500,000
while incrementValue <= 500000:
    # If isAvailable[currentPosition] is True
    if isAvailable[currentPosition]:
        # Set isAvailable[currentPosition] to False
        isAvailable[currentPosition] = False
    
    # Increment incrementValue by 1
    incrementValue += 1
    
    # Update currentPosition
    currentPosition = (currentPosition + incrementValue) % n

# Create a new list availablePositions that includes all True values from isAvailable
availablePositions = [i for i in isAvailable if i]

# Check the length of availablePositions
if len(availablePositions) == 0:
    # Output "YES"
    print("YES")
else:
    # Output "NO"
    print("NO")

# End the program
