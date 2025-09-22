# Read an integer input for the size of the boolean list
n = int(input())

# Initialize the boolean list with all True values
booleanList = [True] * n  # List of size n, initialized to True
index = 0  # Initialize the current index
counter = 1  # Initialize the counter used for movement

# Loop until the counter exceeds 500,000
while counter <= 500000:
    if booleanList[index]:  # If the current list item is True
        booleanList[index] = False  # Mark it as processed (set to False)
    
    counter += 1  # Increment the counter
    index = (index + counter) % n  # Update the index, wrapping around as necessary

# Create a list of remaining True values
remainingTrueValues = [value for value in booleanList if value]

# Determine the output based on the remaining True values
if len(remainingTrueValues) == 0:
    print("YES")  # All values processed
else:
    print("NO")   # Some values remain True
