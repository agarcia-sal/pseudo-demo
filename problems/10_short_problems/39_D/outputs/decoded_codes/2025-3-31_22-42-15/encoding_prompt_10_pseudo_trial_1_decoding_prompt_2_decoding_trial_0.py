def doMain():
    # Get user input for two strings
    t1 = input()
    t2 = input()
    
    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize result counter
    res = 0 
    
    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if the elements are different
        if a != b:
            # Increment result if they are different
            res += 1 
    
    # Determine and print the result based on the counter
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
