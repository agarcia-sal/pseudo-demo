# Begin main process

# Step 1: Gather input
first_input = input()  # Read first input from user
second_input = input()  # Read second input from user

# Step 2: Split input into individual components
first_input_components = first_input.split()  # Split into list of strings
second_input_components = second_input.split()  # Split into list of strings

# Step 3: Initialize a counter for differences
difference_counter = 0  # Counter to track differences

# Step 4: Compare corresponding components from both inputs
for index in range(3):  # Looping from 0 to 2 inclusive
    first_value = int(first_input_components[index])  # Convert to integer
    second_value = int(second_input_components[index])  # Convert to integer

    # If the values are not equal, increment the difference counter
    if first_value != second_value:
        difference_counter += 1  # Increment counter

# Step 5: Determine and output the result based on the number of differences
if difference_counter < 3:
    print("YES")  # Output if differences are less than 3
else:
    print("NO")  # Output if differences are 3 or more

# End main process
