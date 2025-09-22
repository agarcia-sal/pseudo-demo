def do_main():
    # Declare and initialize variables
    t1 = input()
    t2 = input()
    res = 0

    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if elements are different
        if a != b:
            res += 1

    # Check the result count and print appropriate message
    if res < 3:
        print("YES")
    else:
        print("NO")

# Begin execution of the main function
do_main()
