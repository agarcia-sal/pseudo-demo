# Start of the program

# Read an integer input for the size of the list
n = int(input())

# Initialize a boolean list with size n, all set to True
boolean_list = [True] * n

# Initialize starting indices
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    
    # If the current position in list boolean_list is True
    if boolean_list[j]:
        # Mark that position as False
        boolean_list[j] = False  # Set current index to False

    # Increment i
    i += 1
    
    # Update j using the formula and wrapping around with modulo
    j = (j + i) % n

# Create a list x containing positions in boolean_list that are still True
true_positions = [index for index, value in enumerate(boolean_list) if value]

# Check if list true_positions is empty
if len(true_positions) == 0:
    print('YES')  # No True values found
else:
    print('NO')   # There are some True values found

# End of the program
