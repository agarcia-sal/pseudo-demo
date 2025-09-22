def do_main():
    # Initialize input variables
    t1 = input()  # Get first input from the user
    t2 = input()  # Get second input from the user

    # Split the input strings into lists of strings
    tt1 = t1.split()  # Split the first input by spaces
    tt2 = t2.split()  # Split the second input by spaces

    # Initialize result counter
    result_count = 0

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of tt1 to integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to integer

        # Check if elements are different
        if a != b:  # If a and b are not equal
            result_count += 1  # Increment the result counter

    # Check the result count and print the appropriate message
    if result_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Call the main function to execute the code
do_main()
