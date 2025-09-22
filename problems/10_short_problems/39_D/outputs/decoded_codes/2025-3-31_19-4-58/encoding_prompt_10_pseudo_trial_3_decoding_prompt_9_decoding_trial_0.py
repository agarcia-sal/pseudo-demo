def do_main():
    # Initialize variables
    t1 = input()  # User input for the first line
    t2 = input()  # User input for the second line
    res = 0  # Initialize result count to 0

    # Split input strings into lists of strings
    tt1 = t1.split()  # Split the first input string by spaces
    tt2 = t2.split()  # Split the second input string by spaces

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of list 1 to integer
        b = int(tt2[x])  # Convert the x-th element of list 2 to integer
        
        # Check if elements are different
        if a != b:
            res += 1  # Increment the count of differences

    # Check the result count and print the appropriate message
    if res < 3:
        print("YES")
    else:
        print("NO")

# Begin execution of the main function
do_main()
