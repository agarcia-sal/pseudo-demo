# Start the program

# Read an integer input for n
num_elements = int(input())

# Initialize a boolean list of size n with all values set to True
boolean_list = [True] * num_elements

# Initialize two variables j and i
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    # If the current element in list boolean_list at index j is True
    if boolean_list[j] is True:
        # Change the value at index j to False
        boolean_list[j] = False
    
    # Increment i by 1
    i += 1

    # Update j to the next index using modular arithmetic
    j = (j + i) % num_elements

# Create a new list x containing all elements from boolean_list that are still True
true_elements = [value for value in boolean_list if value]

# Check if there are no True values left in true_elements
if len(true_elements) == 0:
    print('YES')  # All positions were marked False
else:
    print('NO')   # There are still True positions left
