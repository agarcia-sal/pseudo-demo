def doMain():
    # Initialize required variables to store input
    t1 = ""
    t2 = ""
    tt1 = []  # List to hold the first line of integers as strings
    tt2 = []  # List to hold the second line of integers as strings
    res = 0   # Count of differing integers

    # Read two lines of input from the user
    t1 = input()  # First line of input
    t2 = input()  # Second line of input

    # Split the input strings into lists of strings based on spaces
    tt1 = t1.split()  # List of first set of integers as strings
    tt2 = t2.split()  # List of second set of integers as strings

    # Compare elements from both lists
    for x in range(3):  # Iterate over the indices 0, 1, and 2
        a = int(tt1[x])  # Convert the string to an integer for tt1
        b = int(tt2[x])  # Convert the string to an integer for tt2
        
        # Check if the integers are not equal
        if a != b:
            res += 1  # Increment the count if they differ

    # Determine the result based on the number of differences
    if res < 3:
        print("YES")  # Print YES if fewer than 3 differences
    else:
        print("NO")   # Print NO if 3 or more differences

# Main execution starts here
doMain()
