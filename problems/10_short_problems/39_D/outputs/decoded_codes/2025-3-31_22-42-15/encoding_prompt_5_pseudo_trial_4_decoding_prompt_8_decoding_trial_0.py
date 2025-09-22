def compare_input_values():
    # Step 1: Accept two sets of inputs
    first_input = input()
    second_input = input()
    
    # Step 2: Split the inputs into separate elements
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):
        # Convert elements from string to integer for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values differ
        if first_value != second_value:
            difference_count += 1
            
    # Step 5: Determine if the inputs are similar based on the count of differences
    if difference_count < 3:
        print("YES")  # At least one value is the same
    else:
        print("NO")   # All values are different

# Step 6: Initiate the program
compare_input_values()
