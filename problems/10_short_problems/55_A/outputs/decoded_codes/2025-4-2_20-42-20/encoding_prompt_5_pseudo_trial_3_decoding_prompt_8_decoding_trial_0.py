# Accept user input for the number of boolean values
numberOfValues = int(input())

# Create a list of boolean values initialized to True
booleanList = [True] * numberOfValues

# Initialize control variables
index = 0
step = 1

# Begin loop that operates until step exceeds 500,000
while step <= 500000:
    # If the current position in the list is still marked as True
    if booleanList[index]:
        # Mark the current position as False (used)
        booleanList[index] = False

    # Increment step to move to the next position
    step += 1
    
    # Calculate the next index to check using the current step and wrap around using modulo
    index = (index + step) % numberOfValues

# Filter out the booleanList to find any remaining True values
remainingTrueValues = [value for value in booleanList if value]

# Check if there are no True values left
if len(remainingTrueValues) == 0:
    # If no True values are left, print "YES"
    print("YES")
else:
    # If there are True values left, print "NO"
    print("NO")
