def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    res = 0  # Initialize the count of differing elements
    
    # Compare elements from both lists
    for x in range(3):  # Loop through each index (0, 1, 2)
        a = int(tt1[x])  # Convert the string to an integer
        b = int(tt2[x])  # Convert the string to an integer
        
        if a != b:  # Check if the values are not equal
            res += 1  # Increment the count of differences
    
    # Determine the result based on the comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
