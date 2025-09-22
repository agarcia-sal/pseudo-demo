# Step 1: Start the program by receiving user input for the number of elements.
number_of_elements = int(input())  # Getting the number of elements

# Step 2: Create a list called "flags" initialized to True for each element.
flags = [True] * number_of_elements  # A list to track the condition of each element

# Step 3: Initialize "index" and "counter" variables.
index = 0  # Represents the current position in the "flags" list
counter = 1  # Controls the number of iterations

# Step 4: Enter a loop that runs until the counter exceeds 500,000.
while counter <= 500000:
    # Check if the current entry in flags is True
    if flags[index]:
        flags[index] = False  # Mark the entry as False
    
    counter += 1  # Increment the counter for the next iteration
    
    # Update index in a circular fashion
    index = (index + counter) % number_of_elements

# Step 5: Create a new list called "active_flags" containing only the True entries.
active_flags = [flag for flag in flags if flag]  # List comprehension to filter True entries

# Step 6: Check the length of the "active_flags" list and output the result.
if len(active_flags) == 0:
    print("YES")  # All entries in flags were set to False
else:
    print("NO")  # Some entries in flags remain True

# Step 7: End the program (implied as the program will naturally end here).
