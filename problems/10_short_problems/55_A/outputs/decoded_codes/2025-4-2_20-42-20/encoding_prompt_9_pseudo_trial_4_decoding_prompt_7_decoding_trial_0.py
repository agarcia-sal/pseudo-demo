# Step 1: Receive Input
n = int(input())  # Read an integer n representing the size of the boolean list.

# Step 2: Initialize Variables
booleanList = [True] * n  # Create a list of size n filled with True values.
index = 0  # Initialize index to track the current position in the list.
counter = 1  # Initialize counter to determine the movement steps.

# Step 3: Loop through a Range
while counter <= 500000:
    if booleanList[index]:  # Check if the current item is True
        booleanList[index] = False  # Mark the item at current index as processed (set to False)
    counter += 1  # Increment the counter
    index = (index + counter) % n  # Update the index with wrap-around using modulo n

# Step 4: Check for Remaining True Values
remainingTrueValues = [value for value in booleanList if value]  # Create a list of remaining True values

# Step 5: Determine Output
if len(remainingTrueValues) == 0:  # If there are no remaining True values
    print("YES")  # All values have been processed
else:
    print("NO")  # Some values remain True
