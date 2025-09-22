# Start Program: Read a number and store it in a variable
number_of_elements = int(input())

# Initialize: Create a boolean list and set pointer and index
boolean_list = [True] * number_of_elements  # List of size number_of_elements initialized to True
pointer = 0
index = 1

# Loop: Modify the boolean_list according to specified conditions
while index <= 500000:
    if boolean_list[pointer]:  # Check if the current element is True
        boolean_list[pointer] = False  # Set the current element to False
    index += 1  # Increment index
    pointer = (pointer + index) % number_of_elements  # Update pointer using modulo arithmetic

# Filter Active Elements: Create a new list for elements that are still True
active_elements = [element for element in boolean_list if element]  # List comprehension to filter

# Check Result: Determine if any active elements remain
if len(active_elements) == 0:  # If there are no True elements left
    print("YES")
else:
    print("NO")
