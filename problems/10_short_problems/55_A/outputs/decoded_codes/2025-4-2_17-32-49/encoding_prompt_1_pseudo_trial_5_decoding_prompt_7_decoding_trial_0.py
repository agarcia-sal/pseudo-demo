# Start of the program

# Step 2: Input a number 'n' (the maximum size of the list)
n = int(input())

# Step 3: Create a list 'isAvailable' of size 'n' and set all elements to True
isAvailable = [True] * n

# Step 4: Initialize the tracking variables
currentPosition = 0
incrementValue = 1

# Step 5: Set a loop to run while 'incrementValue' is less than or equal to 500,000
while incrementValue <= 500000:
    # If the position at 'currentPosition' is True
    if isAvailable[currentPosition]:
        # Mark this position as unavailable
        isAvailable[currentPosition] = False

    # Increment 'incrementValue' by 1
    incrementValue += 1

    # Update 'currentPosition' using modulo to wrap around
    currentPosition = (currentPosition + incrementValue) % n

# Step 6: Create a new list 'availablePositions' with positions that are still True
availablePositions = [i for i in range(n) if isAvailable[i]]

# Step 7: Check the length of 'availablePositions'
if len(availablePositions) == 0:
    # Output "YES" if all positions are unavailable
    print("YES")
else:
    # Output "NO" if there are still available positions
    print("NO")

# End of the program
