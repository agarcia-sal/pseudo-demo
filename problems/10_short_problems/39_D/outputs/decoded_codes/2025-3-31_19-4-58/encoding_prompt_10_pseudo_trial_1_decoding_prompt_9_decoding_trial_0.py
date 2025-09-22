def doMain():
    # Read input from user
    t1 = input()  # Input string 1
    t2 = input()  # Input string 2
    
    # Split the input strings into lists of strings
    tt1 = t1.split()  # Split t1 into a list of strings
    tt2 = t2.split()  # Split t2 into a list of strings
    
    res = 0  # Initialize result count
    
    # Loop through the first three elements
    for x in range(3):
        # Convert strings to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if the values are different
        if a != b:
            res += 1  # Increment the difference counter
    
    # Decide based on the count of differences
    if res < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")  # Three or more differences

# Main program execution
doMain()
