def doMain():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    res = 0 
    
    # Compare corresponding elements of the two lists
    for x in range(3):  # 0 to 2 inclusive
        a = int(tt1[x])  # Convert to integer
        b = int(tt2[x])  # Convert to integer
        
        # Count how many elements are different
        if a != b:  # Check for differences
            res += 1  # Increment counter
    
    # Determine if differences are less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
