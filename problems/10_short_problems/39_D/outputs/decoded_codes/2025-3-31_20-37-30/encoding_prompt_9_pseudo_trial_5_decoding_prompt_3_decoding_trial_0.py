def compare_number_sets():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()
    
    # Step 3: Process Input
    first_numbers = first_set.split()
    second_numbers = second_set.split()
    
    # Step 4: Initialize Differences Counter
    difference_count = 0
    
    # Step 5: Compare Numbers
    for index in range(3):  # We know we are only comparing three numbers
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])
        
        if first_number != second_number:
            difference_count += 1
    
    # Step 6: Determine Output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function to execute the program
compare_number_sets()
