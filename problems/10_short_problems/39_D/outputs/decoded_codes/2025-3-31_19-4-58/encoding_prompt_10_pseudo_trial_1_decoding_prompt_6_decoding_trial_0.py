def do_main():
    # Read input from user
    t1 = input()  # First string input containing space-separated integers
    t2 = input()  # Second string input containing space-separated integers
    
    # Split the input strings into lists of strings
    tt1 = t1.split()  # Splitting the first input
    tt2 = t2.split()  # Splitting the second input
    
    res = 0  # Initialize result count for differing integers
    
    # Loop through the first three elements
    for x in range(3):  # Iterating from 0 to 2
        a = int(tt1[x])  # Convert the x-th element of tt1 to integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to integer
        
        # Check if the values are different
        if a != b:  # If a and b are not equal
            res += 1  # Increment the difference counter
    
    # Decide based on the count of differences
    if res < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Main program execution
do_main()  # Invoke the function to run the program
