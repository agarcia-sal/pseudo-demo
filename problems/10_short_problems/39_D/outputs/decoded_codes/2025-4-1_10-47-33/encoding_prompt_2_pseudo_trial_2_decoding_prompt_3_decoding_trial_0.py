def compare_inputs():
    # Step 2: Receive input
    first_input = input()
    second_input = input()

    # Step 3: Process the inputs
    first_list = first_input.split()
    second_list = second_input.split()
    
    difference_count = 0  # Initialize the count of differing elements

    # Step 4: Compare elements
    for index in range(3):
        # Convert input strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Check for differences
        if first_number != second_number:
            difference_count += 1  # Increment count if numbers differ

    # Step 5: Evaluate the results
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Calling the function to execute the program
compare_inputs()
