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
    for x in range(3):
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Count how many elements are different
        if a != b:
            res += 1 
    
    # Determine if differences are less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()


def doMain():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Ensure both lists have the same length
    if len(tt1) != len(tt2):
        print("Input lists must be of the same length.")
        return

    # Initialize a counter for differences
    res = 0 
    
    # Compare corresponding elements of the two lists
    for x in range(len(tt1)):
        try:
            a = int(tt1[x])
            b = int(tt2[x])
        except ValueError:
            print("Both inputs must contain integers.")
            return
        
        # Count how many elements are different
        if a != b:
            res += 1 
    
    # Determine if differences are less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
