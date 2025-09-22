def doMain():
    # Step 1: Gather Input
    input1 = input()  # User input for the first list
    input2 = input()  # User input for the second list

    # Step 2: Split Inputs into Lists
    list1 = input1.split()  # Split input1 into list1
    list2 = input2.split()  # Split input2 into list2

    # Step 3: Initialize a Result Counter
    resultCounter = 0

    # Step 4: Compare Elements of Both Lists
    for index in range(3):  # Loop over the first three elements
        # Convert current elements to integers
        valueFromList1 = int(list1[index])  # Convert element from list1 to integer
        valueFromList2 = int(list2[index])  # Convert element from list2 to integer

        # Step 5: Check if the values are different
        if valueFromList1 != valueFromList2:  # If the values are different
            resultCounter += 1  # Increment the counter

    # Step 6: Determine the Result
    if resultCounter < 3:  # If differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Otherwise, print NO

# Step 7: Execute the Main Function
doMain()
