def doMain():
    # Step 1: Input Collection
    input1 = input()  # Read the first line of input
    input2 = input()  # Read the second line of input
    
    # Step 2: Data Processing
    list1 = input1.split()  # Split the first input into a list
    list2 = input2.split()  # Split the second input into a list
    differenceCount = 0  # Initialize a counter for differences
    
    # Step 3: Comparison Loop
    for index in range(3):  # Loop through the first three indices (0 to 2)
        valueA = int(list1[index])  # Convert the current value from list1 to an integer
        valueB = int(list2[index])  # Convert the current value from list2 to an integer
        
        # Compare the values from both lists
        if valueA != valueB:
            differenceCount += 1  # Increment the difference count if values are not equal
            
    # Step 4: Output Decision
    if differenceCount < 3:  # Check if the count of differences is less than 3
        print("YES")  # Print "YES" if fewer than 3 differences
    else:
        print("NO")  # Print "NO" otherwise

# Execute the doMain function when the program starts
doMain()
