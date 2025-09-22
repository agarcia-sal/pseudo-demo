def compare_three_integers():
    # Prompt user for input and store as firstInput
    first_input = input()
    # Prompt user for input and store as secondInput
    second_input = input()

    # Split inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize difference counter
    difference_count = 0

    # Compare corresponding values in both lists
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        first_value = int(first_list[index])  # Convert string to integer
        second_value = int(second_list[index])  # Convert string to integer

        # Increment the difference count if the values are not equal
        if first_value != second_value:
            difference_count += 1

    # Check the condition for difference count
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" otherwise

# Execute the function
compare_three_integers()
