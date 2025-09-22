def doMain():
    # Initialize input variables
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize the result counter
    res = 0
    
    # Loop through the first 3 elements of both input lists
    for x in range(3):
        # Convert strings to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Compare elements and update the result counter
        if a != b:
            res += 1
            
    # Check the result to determine output
    if res < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
doMain()
