# Read an integer from input representing the number of elements
numberOfElements = int(input())

# Create a boolean array initialized to True
isAvailable = [True] * numberOfElements

# Initialize index variables
indexDifference = 0
index = 1

# Loop until the index surpasses 500,000
while index <= 500000:
    # If the current index of isAvailable is True
    if isAvailable[indexDifference]:
        # Mark this index as False (not available)
        isAvailable[indexDifference] = False
    
    # Increment index
    index += 1
    
    # Update indexDifference to wrap around using modulus
    indexDifference = (indexDifference + index) % numberOfElements

# Create a list of True values from isAvailable
availableElements = [x for x in isAvailable if x]

# Check if any elements are available
if len(availableElements) == 0:
    print('YES')  # All elements marked as not available
else:
    print('NO')
