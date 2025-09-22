def doMain():
    # Initialize variables
    t1 = ""
    t2 = ""
    tt1 = []
    tt2 = []
    res = 0  # Initialized to 0
    
    # Input two strings containing numbers
    t1 = input()  # User input for string 1
    t2 = input()  # User input for string 2
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Split string t1 by space
    tt2 = t2.split()  # Split string t2 by space
    
    # Loop to compare the first three elements
    for x in range(3):  # Iterate from 0 to 2
        # Convert string elements to integers and assign to variables
        a = int(tt1[x])  # Convert string to integer from tt1
        b = int(tt2[x])  # Convert string to integer from tt2
        
        # Compare the two integers
        if a != b:
            res += 1  # Increment res by 1 if they are not equal
    
    # Determine the result based on the count of differences
    if res < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" if differences are 3 or more

# Entry point for program execution
if __name__ == "__main__":
    doMain()  # Call the main function
