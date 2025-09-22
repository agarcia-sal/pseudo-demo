# Start Program
number_of_elements = int(input())  # Read number of elements

# Initialize
boolean_list = [True] * number_of_elements  # Create a boolean list initialized to True
pointer = 0  # Initialize pointer to 0
index = 1    # Initialize index to 1

# Loop
while index <= 500000:
    if boolean_list[pointer]:  # Check if the current pointer position is True
        boolean_list[pointer] = False  # Set it to False
    index += 1  # Increment the index
    pointer = (pointer + index) % number_of_elements  # Update pointer using modulo

# Filter Active Elements
active_elements = [element for element in boolean_list if element]  # Get all True elements

# Check Result
if len(active_elements) == 0:  # Check if no elements are True
    print("YES")  # Output "YES" if all are False
else:
    print("NO")   # Output "NO" otherwise
