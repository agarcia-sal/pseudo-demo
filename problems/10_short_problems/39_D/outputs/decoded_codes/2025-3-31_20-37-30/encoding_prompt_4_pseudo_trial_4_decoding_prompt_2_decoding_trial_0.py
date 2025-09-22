def doMain():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a result counter
    discrepancyCount = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current element to an integer
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Check if the elements are different
        if a != b:
            discrepancyCount += 1  # Increment discrepancyCount by 1
    
    # Determine if discrepancies are less than 3
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    doMain()
