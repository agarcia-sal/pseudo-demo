def doMain():
    # Input collection
    input1 = input()  # Read the first input line
    input2 = input()  # Read the second input line

    # Data processing
    list1 = input1.split()  # Split the first input into a list
    list2 = input2.split()  # Split the second input into a list
    difference_count = 0  # Initialize a counter variable for differences

    # Comparison loop
    for index in range(3):  # Loop through indices 0 to 2
        value_a = int(list1[index])  # Convert value from list1 to integer
        value_b = int(list2[index])  # Convert value from list2 to integer
        if value_a != value_b:  # Check if the values are different
            difference_count += 1  # Increment the difference count

    # Output decision
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")   # Print NO if differences are 3 or more

# Execute the doMain function when the program starts
doMain()
