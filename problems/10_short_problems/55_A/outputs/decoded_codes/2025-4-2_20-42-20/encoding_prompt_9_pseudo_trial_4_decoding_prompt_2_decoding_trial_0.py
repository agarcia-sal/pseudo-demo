# Step 1: Receive Input
n = int(input())

# Step 2: Initialize Variables
booleanList = [True] * n  # Create a list of size n with all values set to True
index = 0                  # Initialize the index to 0
counter = 1                # Initialize the counter to 1

# Step 3: Loop through a Range
while counter <= 500000:
    if booleanList[index]:          # Check if the current position is True
        booleanList[index] = False   # Mark this position as processed (set to False)
    
    counter += 1                     # Increment the counter
    index = (index + counter) % n    # Update the index with wrap around if necessary

# Step 4: Check for Remaining True Values
remainingTrueValues = [value for value in booleanList if value]  # Gather all True values

# Step 5: Determine Output
if len(remainingTrueValues) == 0:  # Check if there are no remaining True values
    print("YES")                    # Print YES if all values have been processed
else:
    print("NO")                     # Print NO if some values remain True
