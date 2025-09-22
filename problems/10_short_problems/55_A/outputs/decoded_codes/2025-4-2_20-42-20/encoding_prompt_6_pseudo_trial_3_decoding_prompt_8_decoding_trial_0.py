# Read an integer input which represents the size of a list.
listSize = int(input())

# Create a boolean list initialized to True for all indices up to listSize.
booleanList = [True] * listSize

# Initialize variables for iteration.
currentIndex = 0
increment = 1

# Loop until increment reaches 500,000.
while increment <= 500000:
    
    # Check if the current index in the boolean list is True.
    if booleanList[currentIndex] is True:
        
        # Set the current index in the boolean list to False.
        booleanList[currentIndex] = False

    # Increment the counter for the next iteration.
    increment += 1
    
    # Calculate the next index by adding the increment and wrapping around the list using modulus.
    currentIndex = (currentIndex + increment) % listSize

# Create a new list containing all the True values from the boolean list.
remainingTrueValues = [value for value in booleanList if value]

# Check if there are any remaining True values.
if len(remainingTrueValues) == 0:
    
    # If no True values remain, print 'YES'.
    print('YES')
else:
    
    # If there are still True values, print 'NO'.
    print('NO')
