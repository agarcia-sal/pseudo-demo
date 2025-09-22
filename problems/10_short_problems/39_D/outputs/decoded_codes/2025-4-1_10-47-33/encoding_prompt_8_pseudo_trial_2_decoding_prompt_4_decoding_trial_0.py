def compare_three_integers():
    # Input handling
    first_input = input()
    second_input = input()
    
    # Data processing
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize difference counter
    difference_count = 0

    # Comparison loop
    for index in range(3):  # Loop over the first three indices
        first_value = int(first_list[index])    # Convert first list item to integer
        second_value = int(second_list[index])  # Convert second list item to integer
        
        # Check for difference between values
        if first_value != second_value:
            difference_count += 1  # Increment counter for differences

    # Condition check
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" otherwise

# Execution
compare_three_integers()
