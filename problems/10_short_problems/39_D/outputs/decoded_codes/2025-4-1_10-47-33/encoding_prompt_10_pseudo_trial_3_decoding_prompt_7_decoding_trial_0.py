def doMain():
    # Declare variables for input strings and result counter
    t1 = ""
    t2 = ""
    tt1 = []  # List to hold split elements of t1
    tt2 = []  # List to hold split elements of t2
    res = 0   # Initialize result counter to 0
    
    # Input two strings containing numbers
    t1 = input()  # Read first line of input
    t2 = input()  # Read second line of input
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Split the first input string by spaces
    tt2 = t2.split()  # Split the second input string by spaces
    
    # Loop to compare the first three elements
    for x in range(3):  # Iterate over the first three indices
        # Convert string elements to integers
        a = int(tt1[x])  # Convert element from first list
        b = int(tt2[x])  # Convert element from second list
        
        # Compare the two integers
        if a != b:  # Check if integers are not equal
            res += 1  # Increment the counter if they differ
    
    # Determine the result based on the count of differences
    if res < 3:  # If differences are less than 3
        print("YES")  # Print "YES"
    else:
        print("NO")  # Otherwise, print "NO"

# Entry point for program execution
if __name__ == "__main__":
    doMain()  # Call the main function to execute the program
