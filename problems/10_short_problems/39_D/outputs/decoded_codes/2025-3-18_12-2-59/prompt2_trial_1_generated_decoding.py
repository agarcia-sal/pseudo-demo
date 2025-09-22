# Read two lines of input from the user
first_input_string = input()
second_input_string = input()

# Split the input strings into lists of elements
first_input_list = first_input_string.split()
second_input_list = second_input_string.split()

# Initialize a counter for differences
difference_counter = 0 

# Compare elements in the two lists
for index in range(3):
    first_value = int(first_input_list[index])
    second_value = int(second_input_list[index])
    
    # Check if the corresponding values are different
    if first_value != second_value:
        difference_counter += 1

# Evaluate the number of differences and provide output
if difference_counter < 3:
    print("YES")
else:
    print("NO")
