# Begin the program

# Read the integer input for the size of the array
numberOfElements = int(input())

# Initialize a boolean array with 'True' values for each index
isActive = [True] * numberOfElements

currentIndex = 0
incrementValue = 1

# Loop until the incrementValue exceeds 500,000
while incrementValue <= 500000:
    
    # If the current index in the boolean array is still marked as active
    if isActive[currentIndex]:
        
        # Set the current index to inactive
        isActive[currentIndex] = False
    
    # Move to the next increment
    incrementValue += 1
    
    # Update the current index using modulo operation to wrap around the boolean array
    currentIndex = (currentIndex + incrementValue) % numberOfElements

# Create a list of active indices based on the boolean array
activeElements = [i for i in range(len(isActive)) if isActive[i]]

# Check if there are any active elements remaining
if len(activeElements) == 0:
    print('YES')  # No active elements found
else:
    print('NO')   # Active elements still present

# End of the program
