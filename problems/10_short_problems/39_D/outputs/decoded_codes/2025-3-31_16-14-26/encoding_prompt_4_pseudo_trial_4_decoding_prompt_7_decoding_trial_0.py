def doMain():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()  # Splitting the first input by spaces
    tt2 = t2.split()  # Splitting the second input by spaces
    
    # Initialize a counter for differences
    res = 0 
    
    # Compare corresponding elements of the two lists
    for x in range(3):  # Looping through the first three indices
        a = int(tt1[x])  # Convert the string to an integer
        b = int(tt2[x])  # Convert the string to an integer
        
        # Count how many elements are different
        if a != b:  # If the elements are not equal
            res += 1  # Increment the difference counter
    
    # Determine if differences are less than 3
    if res < 3:  # If the number of differences is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Main execution starts here
doMain()
