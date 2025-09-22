def do_main():
    # Read inputs for two sets of three integers
    first_input = input()
    second_input = input()

    # Split inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for mismatches
    mismatch_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the corresponding values are different
        if first_value != second_value:
            # Increment the mismatch count
            mismatch_count += 1

    # Determine if the number of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution
do_main()
