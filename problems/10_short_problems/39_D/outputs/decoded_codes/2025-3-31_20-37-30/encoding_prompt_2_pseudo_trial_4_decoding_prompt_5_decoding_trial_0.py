# Begin main process

# Step 1: Gather input
first_input = input()  # Read first input from user
second_input = input()  # Read second input from user

# Step 2: Split input into individual components
first_input_components = first_input.split()  # Split string into a list of strings
second_input_components = second_input.split()  # Split string into a list of strings

# Step 3: Initialize a counter for differences
difference_counter = 0  # Counter to track number of differences

# Step 4: Compare corresponding components from both inputs
for index in range(3):  # Loop through indices 0 to 2 (inclusive)
    first_value = int(first_input_components[index])  # Convert first input component to an integer
    second_value = int(second_input_components[index])  # Convert second input component to an integer
    
    # If the values are not equal, increment the difference counter
    if first_value != second_value:
        difference_counter += 1  # Increment difference counter by 1

# Step 5: Determine and output the result based on the number of differences
if difference_counter < 3:  # Check if differences are less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End main process
