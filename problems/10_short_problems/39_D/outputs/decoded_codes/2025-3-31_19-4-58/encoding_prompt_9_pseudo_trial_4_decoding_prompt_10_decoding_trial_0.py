def compare_number_sets():
    # Step 2: Receive Input
    first_input = input()
    second_input = input()
    
    # Step 3: Split Input into Individual Numbers
    first_set = first_input.split()
    second_set = second_input.split()
    
    # Initialize a Difference Counter
    difference_count = 0
    
    # Step 5: Compare Corresponding Numbers
    for index in range(3):  # Loop through indices 0, 1, 2
        # Convert to integer
        first_number = int(first_set[index])
        second_number = int(second_set[index])
        
        # Check if numbers are different
        if first_number != second_number:
            difference_count += 1
    
    # Step 6: Check the Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function to execute the program
compare_number_sets()
