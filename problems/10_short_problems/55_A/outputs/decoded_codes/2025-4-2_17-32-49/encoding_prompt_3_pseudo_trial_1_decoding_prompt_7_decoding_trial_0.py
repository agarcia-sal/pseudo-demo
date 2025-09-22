# This program creates a boolean list and modifies it based on specified rules. 
# It eventually checks if any True values remain in the list and outputs "YES" or "NO".

# Read an integer input representing the size of the list
listSize = int(input())

# Create a boolean list initialized to True
booleanList = [True] * listSize

# Start index for the boolean list
index = 0  
# Starting point for the iterative process
currentNumber = 1  

# Loop until currentNumber reaches 500000
while currentNumber <= 500000:
    # If the current index in the boolean list is True
    if booleanList[index]:
        # Mark this index as False
        booleanList[index] = False
    
    # Move to the next number
    currentNumber += 1
    # Update the index using the formula (index + currentNumber) modulo listSize
    index = (index + currentNumber) % listSize

# Create a new list to collect all True values from the boolean list
trueValuesList = [value for value in booleanList if value]

# Check if the list of True values is empty
if len(trueValuesList) == 0:
    # Output 'YES' if no True values are found
    print('YES')
else:
    # Output 'NO' if there are still True values found
    print('NO')
