def doMain():
    # Initialize variables
    t1 = ""
    t2 = ""
    tt1 = []
    tt2 = []
    res = 0

    # Get inputs from user
    t1 = input()
    t2 = input()

    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Loop through the first 3 elements of both input lists
    for x in range(3):
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer
        
        # Compare elements and update result counter
        if a != b:
            res += 1

    # Check result to determine output
    if res < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
doMain()
