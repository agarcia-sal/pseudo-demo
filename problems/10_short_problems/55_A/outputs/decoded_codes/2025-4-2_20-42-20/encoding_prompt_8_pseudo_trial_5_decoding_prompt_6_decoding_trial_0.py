# Start Program
number_of_elements = int(input())  # Read a number from user input

# Initialize
boolean_list = [True] * number_of_elements  # Create a list of True values
pointer = 0  # Initialize pointer to 0
index = 1    # Initialize index to 1

# Loop
while index <= 500000:  # Repeat while index is less than or equal to 500000
    if boolean_list[pointer]:  # If the current element at pointer is True
        boolean_list[pointer] = False  # Set current element to False

    index += 1  # Increment index by 1
    pointer = (pointer + index) % number_of_elements  # Update pointer

# Filter Active Elements
active_elements = [element for element in boolean_list if element]  # Create a list of all True elements

# Check Result
if len(active_elements) == 0:  # If there are no True elements left
    print("YES")  # Print YES
else:
    print("NO")  # Otherwise, print NO
