def do_main():
    # Read input from user
    t1 = input()  # First input string
    t2 = input()  # Second input string
    
    # Split the input strings into lists of strings
    tt1 = t1.split()  # Split the first input
    tt2 = t2.split()  # Split the second input
    
    res = 0  # Initialize result count for differing values
    
    # Loop through the first three elements
    for x in range(3):
        a = int(tt1[x])  # Convert value from first list to integer
        b = int(tt2[x])  # Convert value from second list to integer
        
        # Check if the values are different
        if a != b:
            res += 1  # Increment the difference counter if they are different
    
    # Decide based on the count of differences
    if res < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Main program execution
do_main()
