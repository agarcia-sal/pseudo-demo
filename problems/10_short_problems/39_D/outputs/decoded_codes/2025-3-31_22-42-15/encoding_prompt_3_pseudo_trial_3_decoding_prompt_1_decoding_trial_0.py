def doMain():
    # Step 1: Gather Input
    input1 = input()
    input2 = input()

    # Step 2: Split Inputs into Lists
    list1 = input1.split()
    list2 = input2.split()

    # Step 3: Initialize a Result Counter
    resultCounter = 0

    # Step 4: Compare Elements of Both Lists
    for index in range(3):  # assuming only three elements are being compared
        # Convert current elements to integers
        valueFromList1 = int(list1[index])
        valueFromList2 = int(list2[index])

        # Step 5: Check if the values are different
        if valueFromList1 != valueFromList2:
            resultCounter += 1

    # Step 6: Determine the Result
    if resultCounter < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the Main Function
doMain()
