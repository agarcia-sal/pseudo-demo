def doMain():
    # Initialize variables for input strings and result count
    t1 = ""
    t2 = ""
    res = 0
    
    # Get inputs from user
    t1 = input()  # Enter first line of input
    t2 = input()  # Enter second line of input
    
    # Split input strings into lists
    tt1 = t1.split()  # Split the first input string into a list of strings
    tt2 = t2.split()  # Split the second input string into a list of strings
    
    # Loop through the first 3 elements of both input lists
    for x in range(3):
        # Convert the string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Compare elements and update result counter
        if a != b:
            res += 1  # Increment res by 1 if there's a difference
    
    # Check result to determine output
    if res < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences
    

# Call the main function to execute the program
doMain()
