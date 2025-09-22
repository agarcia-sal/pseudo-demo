# Input: An integer n
n = int(input())

# Initialize a list to track boolean values
booleanList = [True] * n

# Initialize indices
currentIndex = 0
counter = 1

# Loop until counter exceeds 500000
while counter <= 500000:
    # If the current index in the boolean list is True
    if booleanList[currentIndex]:
        # Set the current index to False
        booleanList[currentIndex] = False
    
    # Increment counter
    counter += 1
    
    # Update current index using modular arithmetic
    currentIndex = (currentIndex + counter) % n

# Filter out the True values from the boolean list
filteredList = [x for x in booleanList if x]

# Check the length of the filtered list
if len(filteredList) == 0:
    print("YES")  # All positions were marked False
else:
    print("NO")   # There are still True positions left
