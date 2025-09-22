# Start Program
number_of_elements = int(input())  # Read a number from user input

# Initialize
boolean_list = [True] * number_of_elements  # Create a list with all elements set to True
pointer = 0 
index = 1 

# Loop
while index <= 500000:
    if boolean_list[pointer]:  # Check if the current element is True
        boolean_list[pointer] = False  # Set the current element to False
    index += 1  # Increment index
    pointer = (pointer + index) % number_of_elements  # Update pointer

# Filter Active Elements
active_elements = [element for element in boolean_list if element]  # Get all True elements

# Check Result
if len(active_elements) == 0:
    print("YES")  # Print "YES" if no elements are active
else:
    print("NO")   # Print "NO" if there are active elements
