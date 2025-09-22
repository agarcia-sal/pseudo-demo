def doMain():
    # Read input from user
    t1 = input()  # First string input
    t2 = input()  # Second string input
    
    # Split the input strings into lists of strings
    tt1 = t1.split()  # splits t1 into a list of strings
    tt2 = t2.split()  # splits t2 into a list of strings
    
    # Initialize result count
    res = 0  # Number of differing elements

    # Loop through the first three elements
    for x in range(3):
        # Convert string values to integers
        a = int(tt1[x])  # First integer from first input
        b = int(tt2[x])  # First integer from second input
        
        # Check if the values are different
        if a != b:  # If the integers differ
            res += 1  # Increment the difference counter

    # Decide based on the count of differences
    if res < 3:  # If less than three differences are found
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# Main program execution
doMain()  # Call the doMain function to execute the program
