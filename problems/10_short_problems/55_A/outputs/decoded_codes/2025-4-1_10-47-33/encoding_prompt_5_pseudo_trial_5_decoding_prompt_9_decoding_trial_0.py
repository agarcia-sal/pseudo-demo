# Step 1: Accept the size of the boolean list from user input
n = int(input())

# Step 2: Create a boolean list of size n with all values initially set to True
booleanList = [True] * n

# Step 3: Initialize index variables
currentIndex = 0
increment = 1

# Step 4: Loop to update the boolean list
while increment <= 500000:
    # Step 4a: If the value at the current index is True
    if booleanList[currentIndex] is True:
        # Step 4b: Set the value at the current index to False
        booleanList[currentIndex] = False
    
    # Step 4c: Update the increment and move to the next index
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Wrap around if exceeds n

# Step 5: Check for any True values left in the boolean list
remainingTrueValues = [value for value in booleanList if value is True]

# Step 6: Determine the result based on the presence of True values
if len(remainingTrueValues) == 0:
    print("YES")  # No True values remain
else:
    print("NO")   # There are still True values present
