def doMain():
    # Get user input for two strings
    t1 = input()  # User input for the first string of integers
    t2 = input()  # User input for the second string of integers
    
    # Split input strings into lists
    tt1 = t1.split()  # Split the first string by spaces into a list
    tt2 = t2.split()  # Split the second string by spaces into a list
    
    # Initialize result counter
    res = 0 
    
    # Loop through the first three elements of both lists
    for x in range(3):  # Iterate over the first three elements (indices 0 to 2)
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of tt1 to an integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to an integer
        
        # Check if the elements are different
        if a != b:  # If the two integers are not equal
            res += 1  # Increment result if they are different
    
    # Determine and print the result based on the counter
    if res < 3:  # If the number of differing elements is less than 3
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
