# Start the Program

# Read Input:
n = int(input())  # Read an integer value for the size of the list.

# Initialize List:
statusList = [True] * n  # Create a list of size n with all values set to True.

# Initialize Counters:
currentIndex = 0  # Set the current index to 0.
stepCount = 1     # Set the step count to 1.

# Begin Loop:
while stepCount <= 500000:
    # Check if the value at currentIndex in statusList is True:
    if statusList[currentIndex]:  # If it is True:
        statusList[currentIndex] = False  # Change this value to False.

    stepCount += 1  # Increment stepCount by 1.
    
    # Move to the next index position:
    currentIndex = (currentIndex + stepCount) % n  # Update currentIndex with wrapping.

# Check Active Items:
activeItems = [item for item in statusList if item]  # Create a list of all True values.

# Determine Output:
if len(activeItems) == 0:  # If there are no active items left:
    print('YES')  # Print 'YES'.
else:
    print('NO')  # Print 'NO'.

# End the Program
