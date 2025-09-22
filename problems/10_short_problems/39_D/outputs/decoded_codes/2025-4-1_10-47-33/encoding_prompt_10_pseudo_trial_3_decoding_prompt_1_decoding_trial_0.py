def doMain():
    t1 = ""
    t2 = ""
    tt1 = []
    tt2 = []
    res = 0  # Initialize result count to 0
    
    # Input two strings containing numbers
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Loop to compare the first three elements
    for x in range(3):
        # Convert string elements to integers and assign to variables
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Compare the two integers
        if a != b:
            res += 1  # Increment result count if values are not equal
    
    # Determine the result based on the count of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Entry point for program execution
if __name__ == "__main__":
    doMain()
