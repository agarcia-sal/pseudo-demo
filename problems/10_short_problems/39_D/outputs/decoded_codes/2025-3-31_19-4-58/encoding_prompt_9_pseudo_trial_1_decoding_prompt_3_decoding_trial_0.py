def compare_sets():
    # Receive Input
    first_set = input()
    second_set = input()

    # Process Input
    first_values = first_set.split()
    second_values = second_set.split()

    # Initialize Difference Counter
    difference_count = 0

    # Compare Values
    for index in range(3):  # We expect exactly 3 values in each set
        first_value = float(first_values[index])  # Convert to float variable
        second_value = float(second_values[index])  # Convert to float variable
        
        if first_value != second_value:
            difference_count += 1  # Increment the difference counter if values are not equal

    # Determine Result
    if difference_count < 3:
        print("YES")  # Sets differ in fewer than three positions
    else:
        print("NO")  # Sets differ in three or more positions

# Call the function to execute the logic
compare_sets()
