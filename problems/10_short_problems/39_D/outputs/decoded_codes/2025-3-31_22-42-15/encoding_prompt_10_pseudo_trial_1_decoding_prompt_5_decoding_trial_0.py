def do_main():
    # Get user input for two strings
    t1 = input()
    t2 = input()
    
    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize result counter
    result_counter = 0 
    
    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if the elements are different
        if a != b:
            # Increment result if they are different
            result_counter += 1 
    
    # Determine and print the result based on the counter
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
