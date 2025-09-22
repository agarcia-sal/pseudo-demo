# Start of the Program

# Input Handling: Read an integer value from the user
number_of_elements = int(input())

# Initialization: Create a list of size 'number_of_elements' initialized to True
status_list = [True] * number_of_elements
current_index = 0  # Initialize index variable
step_increment = 1  # Initialize counter variable

# Looping Process: Repeat while step_increment is less than or equal to 500,000
while step_increment <= 500000:
    # Check the value at current_index in the status_list
    if status_list[current_index]:
        status_list[current_index] = False  # Set value to False

    # Increment step_increment by 1
    step_increment += 1
    
    # Update current_index and wrap around using modulo
    current_index = (current_index + step_increment) % number_of_elements

# Filtering Results: Create a list of all True elements
true_values = [value for value in status_list if value]

# Output Handling: Check the length of true_values
if len(true_values) == 0:
    print("YES")  # If no True values, print "YES"
else:
    print("NO")   # Otherwise, print "NO"

# End of the Program
