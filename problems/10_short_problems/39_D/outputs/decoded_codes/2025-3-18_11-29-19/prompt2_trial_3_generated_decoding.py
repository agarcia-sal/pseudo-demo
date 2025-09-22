def doMain():
    # Step 2: Prompt the user for the first input string
    firstInputString = input()
    
    # Step 3: Prompt the user for the second input string
    secondInputString = input()
    
    # Step 4: Split the input strings into lists
    firstInputList = firstInputString.split()
    secondInputList = secondInputString.split()
    
    # Step 6: Initialize differenceCount to zero
    differenceCount = 0
    
    # Step 7: Loop through the first three elements of both lists
    for i in range(3):  # Loop 3 times for the three elements
        # a: Convert to integers
        firstValue = int(firstInputList[i])
        secondValue = int(secondInputList[i])
        
        # b: Check for differences
        if firstValue != secondValue:
            differenceCount += 1
    
    # Step 8: Check if differenceCount is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 9: If this script is executed as the main program, call the doMain function
if __name__ == "__main__":
    doMain()
