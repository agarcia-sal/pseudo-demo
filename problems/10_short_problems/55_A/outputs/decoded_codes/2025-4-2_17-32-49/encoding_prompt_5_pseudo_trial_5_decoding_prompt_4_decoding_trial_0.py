# Start Program

# Input Section
n = int(input())  # Prompt user to enter a number and convert it to an integer

# Initialization
booleanList = [True] * n  # Create a list with n elements, all initially set to True
currentIndex = 0  # Initialize the index
counter = 1  # Initialize the counter

# Loop for Operations
while counter <= 500000:
    if booleanList[currentIndex]:  # Check if the current index is True
        booleanList[currentIndex] = False  # Change it to False
        
    counter += 1  # Increment the counter
    currentIndex = (currentIndex + counter) % n  # Update the index with wrap-around using modulo

# Check Remaining True Values
remainingTrue = [value for value in booleanList if value]  # Create a list of still True elements

# Determine the output based on the length of remaining True values
if len(remainingTrue) == 0:
    print("YES")  # All elements are set to False
else:
    print("NO")  # Some elements are still True

# End Program
