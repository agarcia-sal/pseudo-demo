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
    for index in range(3):
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if values differ
        if first_value != second_value:
            difference_count += 1

    # Condition check and output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the function
compare_three_integers()
