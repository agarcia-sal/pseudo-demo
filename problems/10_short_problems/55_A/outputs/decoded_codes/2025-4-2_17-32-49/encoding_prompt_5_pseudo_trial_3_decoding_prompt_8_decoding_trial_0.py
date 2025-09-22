# Start Program

# Receive Input
n = int(input())  # Read a number n which represents the size of a list

# Initialize Boolean List
booleanList = [True] * n  # Create a list of size n with all elements initialized to True

# Set Up Iteration Variables
currentIndex = 0  # Track the position in booleanList
step = 1  # Step value to dictate marking process

# Mark Elements Process
while step <= 500000:
    # Check Current Position
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False  # Mark this position as False

    # Increment Step Value
    step += 1

    # Calculate Next Position
    currentIndex = (currentIndex + step) % n  # Wrap around if it exceeds the length of the list

# Extract Remaining Unmarked Elements
remainingTrue = [item for item in booleanList if item]  # Collect all True values

# Check Results
if len(remainingTrue) == 0:  # If no unmarked positions
    print("YES")  # All positions were marked
else:
    print("NO")  # At least one position remained unmarked

# End Program
