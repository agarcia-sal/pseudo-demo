# Begin the program

# Read an integer input which determines the size of the array
array_size = int(input())

# Create a list of boolean values initialized to True, with a length equal to array_size
boolean_list = [True] * array_size

# Initialize two counter variables: index for the position and increment for the increment value
index = 0
increment = 1

# Loop until increment exceeds 500000
while increment <= 500000:
    # If the current position in the boolean list is True
    if boolean_list[index]:
        # Mark the current position as False
        boolean_list[index] = False

    # Move to the next increment
    increment += 1

    # Update the index using a modulo operation for circular access
    index = (index + increment) % array_size

# Filter the boolean list to find positions still marked as True
filtered_true_values = [value for value in boolean_list if value]

# Check if there are any True values remaining after the loop
if len(filtered_true_values) == 0:
    print('YES')
else:
    print('NO')
