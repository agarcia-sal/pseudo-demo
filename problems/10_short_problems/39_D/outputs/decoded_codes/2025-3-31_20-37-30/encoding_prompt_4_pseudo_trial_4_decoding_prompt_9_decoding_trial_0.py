def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a result counter for discrepancies
    discrepancy_count = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):  # Assuming we want to compare only the first three elements
        a = int(tt1[index])  # Convert the current element from the first line to an integer
        b = int(tt2[index])  # Convert the current element from the second line to an integer
        
        # Check if the elements are different
        if a != b:
            discrepancy_count += 1  # Increment discrepancy count if they are not equal
    
    # Determine if discrepancies are less than 3
    if discrepancy_count < 3:
        print("YES")  # Print YES if discrepancies are less than 3
    else:
        print("NO")   # Print NO otherwise

# Execute the main function
if __name__ == "__main__":
    do_main()
