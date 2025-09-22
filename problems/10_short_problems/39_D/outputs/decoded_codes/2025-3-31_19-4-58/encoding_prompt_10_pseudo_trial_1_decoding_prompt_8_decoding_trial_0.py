def doMain():
    t1 = input()
    t2 = input()
    
    tt1 = t1.split()  # Splits t1 into a list of strings
    tt2 = t2.split()  # Splits t2 into a list of strings
    
    res = 0  # Initialize result count
    
    # Loop through the first three elements
    for x in range(3):
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer
        
        # Check if the values are different
        if a != b:
            res += 1  # Increment the difference counter
    
    # Decide based on the count of differences
    if res < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Main program execution
doMain()
