# Step 1: Read Input
n = int(input())  # Get the total number of elements from the user.

# Step 2: Initialize the Marking List
markings = [True] * n  # Create a list named 'markings' initialized to True.

# Step 3: Set Initial Variables
index = 0  # Initialize the index
step = 1   # Initialize the step count

# Step 4: Start the Marking Process
while step <= 500000:
    if markings[index]:  # Check if the current item is True
        markings[index] = False  # Mark the current item as False
    
    step += 1  # Increment step by 1
    index = (index + step) % n  # Update index with wrapping using modulo

# Step 5: Check Remaining Marked Items
remainingTrue = [mark for mark in markings if mark]  # List of items still True

# Step 6: Output Result
if len(remainingTrue) == 0:  # If all items are marked as False
    print("YES")  # Output YES
else:
    print("NO")  # Output NO
