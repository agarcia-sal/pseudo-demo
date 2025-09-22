# Start

# Receive Input:
list_size = int(input())  # Get the size of the boolean list from the user

# Initialize Boolean List:
boolean_list = [True] * list_size  # Create a list initialized with True

# Initialize Iteration Variables:
current_index = 0  # Starting index
step = 1  # Initial step size

# Loop through iterations:
while step <= 500000:  # Limit the steps to 500,000
    if boolean_list[current_index]:  # Check if the current position is True
        boolean_list[current_index] = False  # Set the position to False
    
    step += 1  # Increment the step by 1
    current_index = (current_index + step) % list_size  # Update current_index, wrapping around if needed

# Check Remaining True Values:
remaining_true = [val for val in boolean_list if val]  # Create a list of remaining True values

# Output Result:
if len(remaining_true) == 0:  # If no True values remain
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# End
