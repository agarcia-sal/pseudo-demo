# Start Program

# Receive Input
n = int(input())  # Read a number `n` which represents the size of a list.

# Initialize Boolean List
booleanList = [True] * n  # Create a list `booleanList` of size `n`, initialized to True.

# Set Up Iteration Variables
currentIndex = 0  # Initialize `currentIndex` to 0.
step = 1          # Initialize `step` to 1.

# Mark Elements Process
while step <= 500000:  # While `step` is less than or equal to 500000:
    # Check Current Position
    if booleanList[currentIndex]:  # If the value at `booleanList[currentIndex]` is True:
        booleanList[currentIndex] = False  # Mark this position as False.

    # Increment Step Value
    step += 1  # Increase `step` by 1.

    # Calculate Next Position
    currentIndex = (currentIndex + step) % n  # Update `currentIndex` with wrapping.

# Extract Remaining Unmarked Elements
remainingTrue = [value for value in booleanList if value]  # Create a list of unmarked positions.

# Check Results
if len(remainingTrue) == 0:  # If there are no unmarked positions:
    print("YES")  # Print "YES".
else:
    print("NO")  # Otherwise, print "NO".

# End Program
