# Start Program

# Receive Input
n = int(input())  # Read a number which represents the size of the boolean list

# Initialize Boolean List
booleanList = [True] * n  # Create a list of size 'n' initialized to True

# Set Up Iteration Variables
currentIndex = 0  # Initialize the current index to 0
step = 1  # Initialize step to 1

# Mark Elements Process
while step <= 500000:  # Continue until step exceeds 500000
    # Check Current Position
    if booleanList[currentIndex]:  # If the current position is still marked as True
        booleanList[currentIndex] = False  # Mark this position as False (indicating it's marked)
    
    # Increment Step Value
    step += 1  # Increase step by 1
    
    # Calculate Next Position
    currentIndex = (currentIndex + step) % n  # Update the index, wrapping around if necessary

# Extract Remaining Unmarked Elements
remainingTrue = [value for value in booleanList if value]  # List of all elements still marked as True

# Check Results
if len(remainingTrue) == 0:  # If there are no unmarked positions
    print("YES")  # Print YES, indicating all positions were marked
else:
    print("NO")  # Otherwise, print NO indicating at least one position remained unmarked

# End Program
