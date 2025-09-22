# Start Program

# Receive Input
n = int(input())  # Read a number representing the size of a list

# Initialize Boolean List
booleanList = [True] * n  # Create a list of size n where each element is initialized to True

# Set Up Iteration Variables
currentIndex = 0  # This will track the position in booleanList
step = 1  # This will dictate how far to move through the list during marking

# Mark Elements Process
while step <= 500000:
    # Check Current Position
    if booleanList[currentIndex]:  # If the value at booleanList[currentIndex] is True
        booleanList[currentIndex] = False  # Mark this position as False (indicating it has been marked)
    
    # Increment Step Value
    step += 1  # Increase step by 1
    
    # Calculate Next Position
    currentIndex = (currentIndex + step) % n  # Update currentIndex with wrapping around

# Extract Remaining Unmarked Elements
remainingTrue = [value for value in booleanList if value]  # Create a list of all True values remaining

# Check Results
if len(remainingTrue) == 0:  # If the length of remainingTrue is 0
    print("YES")  # Indicating all positions were marked
else:
    print("NO")  # Indicating at least one position remained unmarked

# End Program
