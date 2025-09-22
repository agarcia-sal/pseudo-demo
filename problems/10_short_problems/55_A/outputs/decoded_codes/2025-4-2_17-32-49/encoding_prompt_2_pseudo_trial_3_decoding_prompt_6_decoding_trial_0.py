# Start of the program

# Step 2: Read an integer value for totalNumbers
total_numbers = int(input())

# Step 3: Initialize a list to track the availability of numbers
is_number_available = [True] * total_numbers

# Step 4: Initialize stepCount to 1
step_count = 1

# Step 5: Initialize currentIndex to 0
current_index = 0

# Step 6: Loop while stepCount is less than or equal to 500,000
while step_count <= 500000:
    # Check if the current index position in the list is True
    if is_number_available[current_index]:
        # Set that position in the list to False (number eliminated)
        is_number_available[current_index] = False
    
    # Increment stepCount by 1
    step_count += 1
    
    # Update currentIndex using the formula
    current_index = (current_index + step_count) % total_numbers

# Step 7: Generate a list of numbers that are still available
available_numbers = [number for number in is_number_available if number]

# Step 8: Check if there are any available numbers
if len(available_numbers) == 0:
    # Output "YES" if all numbers are eliminated
    print("YES")
else:
    # Output "NO" if there are still available numbers
    print("NO")

# End of the program
