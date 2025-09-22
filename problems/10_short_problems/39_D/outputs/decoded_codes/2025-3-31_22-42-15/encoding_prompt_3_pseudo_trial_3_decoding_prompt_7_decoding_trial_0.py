def doMain():
    # Step 1: Gather Input
    input1 = input()  # Read first input from the user
    input2 = input()  # Read second input from the user

    # Step 2: Split Inputs into Lists
    list1 = input1.split()  # Split first input into a list of strings
    list2 = input2.split()  # Split second input into a list of strings

    # Step 3: Initialize a Result Counter
    resultCounter = 0  # This counter will track the number of differing elements

    # Step 4: Compare Elements of Both Lists
    for index in range(3):  # Iterate over the first three indices (0 to 2)
        # Convert current elements to integers
        valueFromList1 = int(list1[index])  # Convert the current element of list1
        valueFromList2 = int(list2[index])  # Convert the current element of list2
        
        # Step 5: Check if the values are different
        if valueFromList1 != valueFromList2:  # Check for inequality
            resultCounter += 1  # Increment the counter if values are different

    # Step 6: Determine the Result
    if resultCounter < 3:  # If fewer than 3 differences
        print("YES")  # Output "YES"
    else:  # If 3 or more differences
        print("NO")  # Output "NO"

# Step 7: Execute the Main Function
doMain()  # Call the function to run the program
