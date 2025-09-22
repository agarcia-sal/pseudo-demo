def doMain():
    # Declare and initialize variables
    t1 = ""  # First line of input
    t2 = ""  # Second line of input
    res = 0  # Result counter for differences
    
    # Get inputs from user
    t1 = input()
    t2 = input()
    
    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Ensure there are at least three elements to compare
    for x in range(3):
        # Convert elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
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
