def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    res = 0  # Initialize the result count
    
    # Compare elements from both lists
    for x in range(3):  # Loop over the range of the expected length
        a = int(tt1[x])  # Convert to integer
        b = int(tt2[x])  # Convert to integer
        
        if a != b:  # Check for inequality
            res += 1  # Increment result count if different
            
    # Determine the result based on the comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()


    1 2 3
    1 2 4
    

    5 6 7
    5 6 7
    

    0 0 0
    1 1 1
    

    2 3 4
    2 3 5
    