def do_main():
    # Initialize variables
    t1 = input()  # User input for the first string
    t2 = input()  # User input for the second string
    res = 0  # Counter for differences between the two lists

    # Split input strings into lists of strings
    tt1 = t1.split()  # Split the first input by spaces
    tt2 = t2.split()  # Split the second input by spaces

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of the first list to an integer
        b = int(tt2[x])  # Convert the x-th element of the second list to an integer

        # Check if elements are different
        if a != b:
            res += 1  # Increment the counter if they are different

    # Check the result count and print appropriate message
    if res < 3:
        print("YES")  # Print YES if fewer than 3 differences
    else:
        print("NO")  # Print NO if there are 3 or more differences

# Begin execution of the main function
do_main()
