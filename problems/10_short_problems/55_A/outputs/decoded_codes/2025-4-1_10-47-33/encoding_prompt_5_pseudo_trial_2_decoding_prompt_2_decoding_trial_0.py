# Start of the Program
n = int(input())  # Get a number, `n`, from the user input which represents the size of a list.

# Initialize a List
booleanList = [True] * n  # Create a list named `booleanList` with `n` elements, all set to True.

# Set Up Counters
outerCounter = 1  # Initialize outerCounter starting at 1
innerCounter = 0  # Initialize innerCounter starting at 0

# Elimination Loop
while outerCounter <= 500000:  # While outerCounter is less than or equal to 500000
    if booleanList[innerCounter]:  # If the current element of booleanList at index innerCounter is True
        booleanList[innerCounter] = False  # Set that element to False (indicates elimination)
    
    outerCounter += 1  # Increase outerCounter by 1
    innerCounter = (innerCounter + outerCounter) % n  # Update innerCounter

# Check Remaining Values
remainingTrueValues = [value for value in booleanList if value]  # Create a new list containing all elements from booleanList that remain True.

# Determine Result
if len(remainingTrueValues) == 0:  # If the length of remainingTrueValues is equal to 0
    print('YES')  # Output 'YES'
else:
    print('NO')  # Output 'NO'
