# Step 1: Input
n = int(input())

# Step 2: Initialize the Boolean List
isPresent = [True] * n  # Creates a list of size n with all elements set to True

# Step 3: Set Initial Values
currentIndex = 0
step = 1

# Step 4: Loop Until Step Exceeds 500,000
while step <= 500000:
    # Check if isPresent[currentIndex] is True
    if isPresent[currentIndex]:
        isPresent[currentIndex] = False  # Mark this index as processed

    step += 1  # Increment step by 1
    currentIndex = (currentIndex + step) % n  # Update currentIndex circularly

# Step 5: Collect Unprocessed Indices
unprocessedItems = [i for i in range(n) if isPresent[i]]  # Store indices where value is still True

# Step 6: Check Results
if len(unprocessedItems) == 0:
    print("YES")  # All items were processed
else:
    print("NO")   # There are unprocessed items
