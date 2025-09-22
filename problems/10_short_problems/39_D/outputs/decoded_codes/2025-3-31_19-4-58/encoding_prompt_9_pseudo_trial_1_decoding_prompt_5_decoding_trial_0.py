# Start program

# Receive input for the two sets of values
first_set = input()
second_set = input()

# Process input by splitting the sets into individual values
first_set_values = first_set.split()
second_set_values = second_set.split()

# Initialize a counter to track the number of differences
difference_count = 0

# Compare the values at each index
for index in range(3):  # Loop through indices 0 to 2
    # Convert the values from the sets to numbers
    first_value = int(first_set_values[index])
    second_value = int(second_set_values[index])
    
    # Check if the values differ
    if first_value != second_value:
        difference_count += 1  # Increment the difference counter

# Determine the result based on the difference count
if difference_count < 3:
    print("YES")  # Indicate the sets differ in fewer than three positions
else:
    print("NO")   # Indicate the sets differ in three or more positions

# End program
