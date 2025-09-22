# Step 1: Read an integer value 'n' which represents the number of elements.
number_of_elements = int(input())

# Step 2: Create a list 'b' of size 'n', filled with 'True' values.
marked_positions = [True] * number_of_elements

# Step 3: Initialize variables 'j' to 0 and 'i' to 1
j = 0
i = 1

# Step 4: Loop while 'i' is less than or equal to 500,000
while i <= 500000:
    # Step 5: Check if the value at position 'j' in 'b' is True
    if marked_positions[j]:
        # Mark the current position as False
        marked_positions[j] = False
    
    # Step 6: Increment 'i'
    i += 1
    
    # Step 7: Update 'j' using modulo to wrap around
    j = (j + i) % number_of_elements

# Step 8: Create a new list 'x' of all True values from 'marked_positions'
remaining_true_positions = [value for value in marked_positions if value]

# Step 9: Check the length of 'remaining_true_positions'
if len(remaining_true_positions) == 0:
    # If the length is zero, print "YES"
    print("YES")
else:
    # Else, print "NO"
    print("NO")
