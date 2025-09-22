def compare_number_sets():
    # Step 2: Receive Input
    first_set_input = input()
    second_set_input = input()

    # Step 3: Split Input into Individual Numbers
    first_set = first_set_input.split()
    second_set = second_set_input.split()

    # Step 4: Initialize a Difference Counter
    difference_count = 0

    # Step 5: Compare Corresponding Numbers
    for i in range(3):  # We expect exactly three numbers in each set
        first_number = int(first_set[i])  # Convert to integer
        second_number = int(second_set[i])  # Convert to integer
        
        if first_number != second_number:
            difference_count += 1  # Increment count if numbers are different

    # Step 6: Check the Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function to run the program
compare_number_sets()
