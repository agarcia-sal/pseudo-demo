def doMain():
    # Step 1: Input Collection
    input1 = input()  # Read first line of input
    input2 = input()  # Read second line of input

    # Step 2: Data Processing
    list1 = input1.split()  # Split input1 into a list
    list2 = input2.split()  # Split input2 into a list
    difference_count = 0  # Initialize a counter for differences

    # Step 3: Comparison Loop
    for index in range(3):  # Loop through indices 0 to 2
        valueA = int(list1[index])  # Convert value from list1 to integer
        valueB = int(list2[index])  # Convert value from list2 to integer
        if valueA != valueB:  # Check if the values are different
            difference_count += 1  # Increment the difference counter

    # Step 4: Output Decision
    if difference_count < 3:  # Check the count of differences
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Execute the doMain function when the program starts
doMain()
