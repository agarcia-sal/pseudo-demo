def CompareInputValues():
    # Step 1: Accept two sets of inputs
    firstInput = input()
    secondInput = input()
    
    # Step 2: Split the inputs into separate elements
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 3: Initialize a counter for differences
    differenceCount = 0
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):
        # Convert elements from string to integer for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values differ
        if firstValue != secondValue:
            differenceCount += 1
    
    # Step 5: Determine if the inputs are similar based on the count of differences
    if differenceCount < 3:
        print("YES")  # At least one value is the same
    else:
        print("NO")   # All values are different

# Step 6: Initiate the program
CompareInputValues()
