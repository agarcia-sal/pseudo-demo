def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    res = 0 
    
    # Compare corresponding elements of the two lists
    for x in range(3):  # Assuming the input lists are always of length 3
        a = int(tt1[x])  # Convert the string to an integer
        b = int(tt2[x])  # Convert the string to an integer
        
        # Count how many elements are different
        if a != b:
            res += 1  # Increment differences counter

    # Determine if differences are less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
