def do_main():
    # Read input from the user
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists of strings
    tt1 = t1.split()  # splits t1 into a list of strings
    tt2 = t2.split()  # splits t2 into a list of strings
    
    # Initialize the count of differences
    difference_count = 0
    
    # Loop through the first three elements
    for x in range(3):
        a = int(tt1[x])  # convert string at position x from tt1 to integer
        b = int(tt2[x])  # convert string at position x from tt2 to integer
        
        # Check if the values are different
        if a != b:
            difference_count += 1  # Increment the difference counter
    
    # Decide based on the count of differences
    if difference_count < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")  # Three or more differences

# Main program execution
do_main()
