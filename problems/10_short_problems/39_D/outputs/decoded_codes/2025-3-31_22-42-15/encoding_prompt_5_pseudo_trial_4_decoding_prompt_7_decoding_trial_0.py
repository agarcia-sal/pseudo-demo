def compare_input_values():
    # Step 1: Accept two sets of inputs
    first_input = input()  # Read the first line of input from the user
    second_input = input()  # Read the second line of input from the user
    
    # Step 2: Split the inputs into separate elements
    first_list = first_input.split()  # Split the first input into a list
    second_list = second_input.split()  # Split the second input into a list
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert elements from string to integer for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values differ
        if first_value != second_value:  # Compare the two values
            difference_count += 1  # Increment the difference counter
    
    # Step 5: Determine if the inputs are similar based on the count of differences
    if difference_count < 3:  # If fewer than 3 values are different
        print("YES")  # At least one value is the same
    else:
        print("NO")  # All values are different

# Step 6: Initiate the program
compare_input_values()
