def doMain():
    # Step 1: Read input values
    firstInput = input()
    secondInput = input()
    
    # Step 2: Split the input strings into lists of words
    firstInputList = firstInput.split()
    secondInputList = secondInput.split()
    
    # Step 3: Initialize a counter for differences
    differenceCount = 0
    
    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert string elements to integers for comparison
        valueFromFirstList = int(firstInputList[index])
        valueFromSecondList = int(secondInputList[index])
        
        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:
            differenceCount += 1

    # Step 5: Determine result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    doMain()
