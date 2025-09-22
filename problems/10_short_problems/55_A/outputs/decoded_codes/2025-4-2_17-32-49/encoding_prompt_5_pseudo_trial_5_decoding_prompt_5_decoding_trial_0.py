# Begin the program

# Input section
n = int(input())  # Read an integer input from the user, representing the number of elements

# Initialization
boolean_list = [True] * n  # Create a list with n elements, all initialized to True
current_index = 0  # Initialize the current index to 0
counter = 1  # Initialize the counter to 1

# Loop for operations
while counter <= 500000:
    if boolean_list[current_index]:  # Check if the current element is True
        boolean_list[current_index] = False  # Set the current element to False
    
    counter += 1  # Increment the counter by 1
    current_index = (current_index + counter) % n  # Update the current index

# Check remaining true values
remaining_true = [value for value in boolean_list if value]  # Create a list of remaining True elements

# Determine output based on the length of remaining_true
if len(remaining_true) == 0:
    print("YES")  # All elements have been set to False
else:
    print("NO")  # Some elements are still True
