def doMain():
    # Step 2: Read two strings from user input
    firstInput = input()
    secondInput = input()

    # Step 3: Split the firstInput into a list of strings
    firstList = firstInput.split()
    
    # Step 4: Split the secondInput into a list of strings
    secondList = secondInput.split()
    
    # Step 5: Initialize differencesCount to zero
    differencesCount = 0
    
    # Step 6: Loop to check each index from 0 to 2
    for i in range(3):
        # Get integer values from each list
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Step 6: Check for differences
        if firstValue != secondValue:
            differencesCount += 1
    
    # Step 7: Output based on the count of differences
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")
    
# Step 8: Check if the script is executed directly
if __name__ == "__main__":
    doMain()
