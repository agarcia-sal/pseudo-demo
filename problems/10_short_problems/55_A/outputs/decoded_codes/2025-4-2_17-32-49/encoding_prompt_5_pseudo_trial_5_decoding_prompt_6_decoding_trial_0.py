# Start Program

# Input Section: Prompt the user to enter a number and convert it to an integer.
number_of_elements = int(input())

# Initialization: Create a list with n elements, all initially set to True.
boolean_list = [True] * number_of_elements
current_index = 0  # Initialize current index
counter = 1  # Initialize counter

# Loop for Operations: Perform the logic until counter exceeds 500,000
while counter <= 500000:
    if boolean_list[current_index]:  # Check if the current element is True
        boolean_list[current_index] = False  # Set it to False
    
    counter += 1  # Increment counter
    current_index = (current_index + counter) % number_of_elements  # Update index using modulo

# Check Remaining True Values: Create a list to hold the remaining True values
remaining_true = [value for value in boolean_list if value]

# Output results based on the length of remaining_true
if len(remaining_true) == 0:
    print("YES")  # All elements are set to False
else:
    print("NO")  # Some elements are still True

# End Program
