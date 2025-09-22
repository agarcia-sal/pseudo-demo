def doMain():
    # Initialize variables
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    res = 0
    
    # Compare elements from both lists
    for x in range(3):  # Loop from 0 to 2
        a = int(tt1[x])  # Convert to integer
        b = int(tt2[x])  # Convert to integer
        
        # Increment res if elements are not equal
        if a != b:
            res += 1
    
    # Determine the result based on the comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
