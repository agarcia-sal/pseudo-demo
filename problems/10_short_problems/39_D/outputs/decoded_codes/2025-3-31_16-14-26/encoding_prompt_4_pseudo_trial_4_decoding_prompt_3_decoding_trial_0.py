def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    differences_count = 0 
    
    # Compare corresponding elements of the two lists
    for index in range(3):  # Loop from 0 to 2
        a = int(tt1[index])  # Convert string to integer
        b = int(tt2[index])  # Convert string to integer
        
        # Count how many elements are different
        if a != b:
            differences_count += 1 
    
    # Determine if differences are less than 3
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
