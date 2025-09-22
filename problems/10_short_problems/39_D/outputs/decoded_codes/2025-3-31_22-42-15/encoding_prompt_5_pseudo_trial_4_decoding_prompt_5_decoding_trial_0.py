def compare_input_values():
    # Step 1: Accept two sets of inputs
    first_input = input()  # Read first line of input
    second_input = input()  # Read second line of input
    
    # Step 2: Split the inputs into separate elements
    first_list = first_input.split()  # Split first input into a list
    second_list = second_input.split()  # Split second input into a list
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert elements from string to integer for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values differ
        if first_value != second_value:
            difference_count += 1  # Increment counter if values are different
    
    # Step 5: Determine if the inputs are similar based on the count of differences
    if difference_count < 3:  # If at least one value is the same
        print("YES")
    else:  # All values are different
        print("NO")

# Step 6: Initiate the program
compare_input_values()
