def do_main():
    # Read two lines of input from the user
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a result counter for discrepancies
    discrepancy_count = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):
        # Convert the current elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Check if the elements are different
        if a != b:
            discrepancy_count += 1
    
    # Determine if discrepancies are less than 3
    if discrepancy_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is running as main
if __name__ == "__main__":
    do_main()
