def doMain():
    # Initialization of variables
    t1 = ""  # Input string for first list
    t2 = ""  # Input string for second list
    res = 0  # Result count initialized to 0
    tt1 = []  # List to hold split string of t1
    tt2 = []  # List to hold split string of t2

    # Get user input
    t1 = input()
    t2 = input()

    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of tt1 to integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to integer

        # Check if elements are different
        if a != b:
            res += 1  # Increment res by 1 if a and b are not equal

    # Check the result count and print appropriate message
    if res < 3:
        print("YES")
    else:
        print("NO")

# Begin execution of the main function
doMain()
