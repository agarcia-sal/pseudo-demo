def doMain():
    # Declare t1 and t2 as strings and take user input
    t1 = input()  # Read input from user
    t2 = input()  # Read input from user
    
    # Split the input strings into lists
    tt1 = t1.split()  # splits t1 into a list of strings
    tt2 = t2.split()  # splits t2 into a list of strings
    
    # Initialize result count
    res = 0  # Initialize result count
    
    # Loop through the first three elements
    for x in range(3):  # loop from 0 to 2
        # Convert string elements to integer
        a = int(tt1[x])  # convert tt1[x] to INTEGER
        b = int(tt2[x])  # convert tt2[x] to INTEGER
        
        # Check if the values are different
        if a != b:  # if a is not equal to b
            res += 1  # Increment the difference counter
    
    # Decide based on the count of differences
    if res < 3:  # if res is less than 3
        print("YES")  # Less than three differences
    else:
        print("NO")  # Three or more differences

# Main program execution
doMain()
