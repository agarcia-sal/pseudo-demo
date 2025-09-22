# Start Program

# Receive Input
first_set = input()       # Read the first line and store it as first_set
second_set = input()      # Read the second line and store it as second_set

# Process Input
first_set_values = first_set.split()  # Split first_set into individual values
second_set_values = second_set.split()  # Split second_set into individual values

# Initialize Difference Counter
difference_count = 0  # Counter for differences between the two sets

# Compare Values
for index in range(3):  # Loop through indices 0 to 2
    first_value = int(first_set_values[index])    # Convert to integer
    second_value = int(second_set_values[index])   # Convert to integer
    if first_value != second_value:  # Check if the values are different
        difference_count += 1  # Increment the difference count

# Determine Result
if difference_count < 3:  # Check if the count of differences is less than 3
    print("YES")  # Output YES
else:
    print("NO")   # Output NO

# End Program
