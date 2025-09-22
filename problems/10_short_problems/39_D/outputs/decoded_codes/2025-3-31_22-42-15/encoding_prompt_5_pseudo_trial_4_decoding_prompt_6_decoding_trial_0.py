def compare_input_values():
    # Step 1: Accept two sets of inputs
    first_input = input()  # User inputs first set of values
    second_input = input()  # User inputs second set of values
    
    # Step 2: Split the inputs into separate elements
    first_list = first_input.split()  # Splitting input into a list
    second_list = second_input.split()  # Splitting input into another list
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):  # Looping over the range of 3
        # Convert elements from string to integer for comparison
        first_value = int(first_list[index])  # Parsing the integer from the first list
        second_value = int(second_list[index])  # Parsing the integer from the second list
        
        # Check if the values differ
        if first_value != second_value:  # Comparing the values
            difference_count += 1  # Incrementing the difference counter if they differ
    
    # Step 5: Determine if the inputs are similar based on the count of differences
    if difference_count < 3:  # Checking if fewer than 3 values differ
        print("YES")  # At least one value is the same
    else:
        print("NO")  # All values are different

# Step 6: Initiate the program
compare_input_values()
