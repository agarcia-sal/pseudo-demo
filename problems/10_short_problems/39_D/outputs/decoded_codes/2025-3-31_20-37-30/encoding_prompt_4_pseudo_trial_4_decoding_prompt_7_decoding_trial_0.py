def doMain():
    # Read two lines of input from the user
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a result counter for discrepancies
    discrepancyCount = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):  # We expect exactly three elements
        # Convert the current elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Check if the elements are different
        if a != b:
            discrepancyCount += 1  # Increment discrepancy count
    
    # Determine if discrepancies are less than 3
    if discrepancyCount < 3:
        print("YES")  # Print "YES" if discrepancies are fewer than 3
    else:
        print("NO")   # Print "NO" otherwise

# Execute the main function if the script is running as the main program
if __name__ == "__main__":
    doMain()
