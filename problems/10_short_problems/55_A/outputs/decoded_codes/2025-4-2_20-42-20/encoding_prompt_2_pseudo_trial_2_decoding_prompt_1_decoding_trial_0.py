# Step 1: Start the program by receiving an integer input
number_of_elements = int(input())

# Step 2: Create a list called "flags" with "number_of_elements" entries, all initially True
flags = [True] * number_of_elements

# Step 3: Initialize two variables
index = 0
counter = 1

# Step 4: Enter a loop that continues as long as "counter" is <= 500,000
while counter <= 500000:
    # Within the loop: check if current entry in "flags" at "index" is True
    if flags[index]:
        flags[index] = False  # Set that entry to False

    # Increment "counter"
    counter += 1
    
    # Update "index"
    index = (index + counter) % number_of_elements  # Wrap around logic

# Step 5: Create a new list called "active_flags" with entries still True
active_flags = [flag for flag in flags if flag]

# Step 6: Check the length of "active_flags"
if len(active_flags) == 0:
    print("YES")  # If empty
else:
    print("NO")   # If not empty

# Step 7: End the program
