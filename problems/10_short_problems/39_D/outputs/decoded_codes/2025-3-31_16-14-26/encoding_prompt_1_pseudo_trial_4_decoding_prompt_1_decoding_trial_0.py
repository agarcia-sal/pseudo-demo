def StartMain():
    # Read two lines of input
    input1 = input()
    input2 = input()

    # Split the input strings into lists of values
    values1 = input1.split()
    values2 = input2.split()

    # Initialize a counter for discrepancies
    countDiscrepancies = 0 

    # Compare the elements of both lists up to the first three elements
    for index in range(3):  # Note: Adjustments may be necessary if the lists have fewer than 3 elements
        # Convert the current elements to integers
        valueA = int(values1[index])
        valueB = int(values2[index])
        
        # If the values are not equal, increment the discrepancy counter
        if valueA != valueB:
            countDiscrepancies += 1 

    # If there are fewer than three discrepancies, print "YES"; otherwise print "NO"
    if countDiscrepancies < 3:
        print("YES")
    else:
        print("NO")

# Start the main process
StartMain()
