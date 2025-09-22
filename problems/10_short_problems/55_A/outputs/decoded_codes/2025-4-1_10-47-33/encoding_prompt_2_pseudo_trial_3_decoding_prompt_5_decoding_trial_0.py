# Start of the Program

# Input Handling
number_of_elements = int(input())  # Read an integer value from the user

# Initialization
status_list = [True] * number_of_elements  # Create a list initialized to True
current_index = 0  # Set the starting index
step_increment = 1  # Initialize step increment

# Looping Process
while step_increment <= 500000:  # Repeat while step_increment is within limit
    if status_list[current_index]:  # Check if the current index is True
        status_list[current_index] = False  # Set the value at current index to False
    
    step_increment += 1  # Increment step_increment
    current_index = (current_index + step_increment) % number_of_elements  # Update current index with wrap-around

# Filtering Results
true_values = [value for value in status_list if value]  # List of True values

# Output Handling
if len(true_values) == 0:  # Check if there are no True values left
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End of the Program
