def compare_number_sets():
    # Receive input for the first set of numbers
    first_set = [int(input()) for _ in range(3)]
    
    # Receive input for the second set of numbers
    second_set = [int(input()) for _ in range(3)]
    
    # Initialize the difference count
    difference_count = 0
    
    # Loop through the sets to count differences
    for index in range(3):
        if first_set[index] != second_set[index]:
            difference_count += 1
    
    # Check the number of differences and print result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Run the program
compare_number_sets()
