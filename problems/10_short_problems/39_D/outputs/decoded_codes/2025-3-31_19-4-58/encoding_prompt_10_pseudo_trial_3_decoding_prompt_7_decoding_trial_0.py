def doMain():
    # Declare variables for user input and result
    t1 = input()  # Get user input for the first string
    t2 = input()  # Get user input for the second string
    res = 0  # Initialize result count to zero
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Split the first string by spaces into a list
    tt2 = t2.split()  # Split the second string by spaces into a list

    # Loop through the first three elements of both lists
    for x in range(3):  # Looping index from 0 to 2
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of the first list
        b = int(tt2[x])  # Convert the x-th element of the second list
        
        # Check if elements are different
        if a != b:  # If the two converted integers are not equal
            res += 1  # Increment the result count

    # Check the result count and print the appropriate message
    if res < 3:  # If the count of differences is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Begin execution of the main function
doMain()
