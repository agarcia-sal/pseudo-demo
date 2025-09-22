def doMain():
    # Step 2: Prompt the user to enter the first set of values
    firstSet = input()
    
    # Prompt the user to enter the second set of values
    secondSet = input()
    
    # Split the input strings into lists
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Step 3: Loop through each index from 0 to 2
    for index in range(3):
        # Convert the values at the current index to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are not equal
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1
    
    # Step 4: Check the number of differences
    if differenceCount < 3:
        print("YES")  # Output "YES"
    else:
        print("NO")   # Output "NO"

# Step 5: Execute the doMain function when the program starts
doMain()
