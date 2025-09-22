def doMain():
    # Prompt the user for input and read two lines containing numeric values
    first_sequence = input().split()
    second_sequence = input().split()

    # Initialize a variable to count the differences
    difference_count = 0

    # Compare corresponding values in the two sequences
    for index in range(3):
        first_value = int(first_sequence[index])
        second_value = int(second_sequence[index])
        
        if first_value != second_value:
            # Increment the difference count if values are not equal
            difference_count += 1

    # Determine output based on differences count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
doMain()
