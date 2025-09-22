# Start the program
number_of_elements = int(input())
boolean_list = [True] * number_of_elements
position = 0
increment = 1

# Repeat the following steps while increment is less than or equal to 500,000
while increment <= 500000:
    # Check if the current entry in boolean_list at index position is True
    if boolean_list[position]:
        # If it is True, set that entry to False
        boolean_list[position] = False

    # Increase increment by 1
    increment += 1
    
    # Update position to be the current position plus increment, and use modulus
    position = (position + increment) % number_of_elements

# Create a new list called remaining_true_values
remaining_true_values = [value for value in boolean_list if value]

# If the length of remaining_true_values is equal to 0
if len(remaining_true_values) == 0:
    # Output 'YES'
    print("YES")
else:
    # Otherwise output 'NO'
    print("NO")
