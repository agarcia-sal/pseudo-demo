def doMain():
    # Step 1: Input Collection
    input1 = input()
    input2 = input()

    # Step 2: Data Processing
    list1 = input1.split()
    list2 = input2.split()
    differenceCount = 0

    # Step 3: Comparison Loop
    for i in range(3):  # Loop from index 0 to 2 inclusive
        valueA = int(list1[i])  # Convert current value from list1 to integer
        valueB = int(list2[i])  # Convert current value from list2 to integer
        if valueA != valueB:  # Check if the values are different
            differenceCount += 1  # Increment the difference counter

    # Step 4: Output Decision
    if differenceCount < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")   # 3 or more differences

# Execute the function when the program starts
doMain()
