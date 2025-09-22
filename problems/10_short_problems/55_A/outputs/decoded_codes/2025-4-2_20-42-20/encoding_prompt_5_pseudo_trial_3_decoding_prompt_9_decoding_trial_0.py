# Accept user input for the number of boolean values
number_of_values = int(input())

# Create a list of boolean values initialized to True
boolean_list = [True] * number_of_values

# Initialize control variables
index = 0
step = 1

# Begin loop that operates until step exceeds 500,000
while step <= 500000:
    # If the current position in the list is still marked as True
    if boolean_list[index] is True:
        # Mark the current position as False (used)
        boolean_list[index] = False
    
    # Increment step to move to the next position
    step += 1
    
    # Calculate the next index to check using the current step and wrap around using modulo
    index = (index + step) % number_of_values

# Filter out the boolean_list to find any remaining True values
remaining_true_values = [value for value in boolean_list if value is True]

# Check if there are no True values left
if len(remaining_true_values) == 0:
    # If no True values are left, print "YES"
    print("YES")
else:
    # If there are True values left, print "NO"
    print("NO")
