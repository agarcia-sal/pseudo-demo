# Start of the program

# Input section: Read an integer number `n` from user input
n = int(input())

# Initialization of the boolean list and other variables
booleanList = [True] * n  # Create a list with n elements set to True
currentIndex = 0  # Initialize the current index to 0
counter = 1  # Start the counter at 1

# Loop for operations, up to a maximum of 500000 iterations
while counter <= 500000:
    # Check if the current element in the boolean list is True
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False  # Set the current element to False

    counter += 1  # Increment the counter
    # Update currentIndex to wrap around using modulo operator
    currentIndex = (currentIndex + counter) % n

# Check for remaining True values in the boolean list
remainingTrue = [elem for elem in booleanList if elem]  # Create a list of remaining True elements

# Determine the output based on remaining True values
if len(remainingTrue) == 0:
    print("YES")  # Print "YES" if all values are set to False
else:
    print("NO")  # Print "NO" if some values are still True
