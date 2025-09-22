def doMain():
    # Declare variables
    t1 = ""  # Declaration not necessary in Python, but initializing to empty string
    t2 = ""
    res = 0  # Initialize result counter
    
    # Get user input for two strings
    t1 = input()
    t2 = input()
    
    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Loop through the first three elements of both lists
    for x in range(3):  # range(3) gives 0, 1, 2
        # Convert string elements to integers
        a = int(tt1[x])  # Convert element to integer
        b = int(tt2[x])  # Convert element to integer
        
        # Check if the elements are different
        if a != b:  # If they are not equal
            # Increment result if they are different
            res += 1
    
    # Determine and print the result based on the counter
    if res < 3:  # If result is less than 3
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
