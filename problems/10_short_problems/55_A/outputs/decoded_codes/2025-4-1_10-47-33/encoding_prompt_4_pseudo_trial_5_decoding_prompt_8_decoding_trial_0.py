# Read an integer from input representing the number of elements
number_of_elements = int(input())

# Create a boolean array initialized to True
is_available = [True] * number_of_elements

# Initialize index variables
index_difference = 0
index = 1

# Loop until the index surpasses 500,000
while index <= 500000:
    # If the current index of is_available is True
    if is_available[index_difference]:
        # Mark this index as False (not available)
        is_available[index_difference] = False
    
    # Increment index
    index += 1
    
    # Update index_difference to wrap around using modulus
    index_difference = (index_difference + index) % number_of_elements

# Create a list of True values from is_available
available_elements = [i for i in is_available if i]

# Check if any elements are available
if len(available_elements) == 0:
    print('YES')  # All elements marked as not available
else:
    print('NO')
