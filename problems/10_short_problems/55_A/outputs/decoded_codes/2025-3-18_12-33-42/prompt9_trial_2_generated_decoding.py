# Initialize Input
number_of_elements = int(input())  # Read an integer value

# Create a List
boolean_list = [True] * number_of_elements  # Initialize the list with True values

# Set Initial Indexes
current_index = 0
step = 1

# Process the List
while step <= 500000:
    if boolean_list[current_index]:  # Check if the value is True
        boolean_list[current_index] = False  # Set it to False
    step += 1  # Increment step
    current_index = (current_index + step) % number_of_elements  # Update currentIndex

# Check Remaining Values
remaining_true_values = [value for value in boolean_list if value]  # List of True values

# Output Result
if len(remaining_true_values) == 0:  # No True values remaining
    print("YES")
else:
    print("NO")
