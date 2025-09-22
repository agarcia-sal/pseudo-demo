def compare_sets():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Split Input into Individual Numbers
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Step 4: Initialize Difference Count
    difference_count = 0

    # Step 5: Compare the Numbers
    for i in range(3):  # We know there are exactly 3 numbers in each set
        first_number = int(first_numbers[i])
        second_number = int(second_numbers[i])
        
        if first_number != second_number:
            difference_count += 1

    # Step 6: Evaluate Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function to execute the program
compare_sets()
