# Start the program
# Get a number 'n' from the user which indicates the size of the list
size_of_list = int(input())

# Initialize a list 'boolean_list' with 'n' elements all set to TRUE (or True in Python)
boolean_list = [True] * size_of_list

# Set variable 'index' to 0
current_index = 0

# Set variable 'increment' to 1
increment_value = 1

# WHILE increment is less than or equal to 500000
while increment_value <= 500000:
    # IF boolean_list at position 'current_index' is TRUE THEN
    if boolean_list[current_index]:
        # Set boolean_list at position 'current_index' to FALSE
        boolean_list[current_index] = False
    
    # Increase increment by 1
    increment_value += 1
    
    # Update index to (index + increment) modulo n to wrap around if it exceeds n
    current_index = (current_index + increment_value) % size_of_list

# Create a new list 'remaining_true' that contains all TRUE values from boolean_list
remaining_true = [value for value in boolean_list if value]

# IF the length of remaining_true is 0 THEN
if len(remaining_true) == 0:
    # PRINT "YES"
    print("YES")
else:
    # ELSE: PRINT "NO"
    print("NO")

# End the program
