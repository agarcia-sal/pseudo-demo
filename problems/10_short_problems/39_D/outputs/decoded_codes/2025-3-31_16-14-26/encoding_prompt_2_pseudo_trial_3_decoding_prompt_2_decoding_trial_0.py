def doMain():
    # Step 1: Prompt for input
    firstInput = input()
    secondInput = input()
    
    # Step 2: Split the input strings into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Step 3: Initialize the difference count
    differenceCount = 0
    
    # Step 4: Iterate through the values for three iterations
    for i in range(3):
        firstValue = int(firstValues[i])  # Convert to integer
        secondValue = int(secondValues[i])  # Convert to integer
        
        # Step 5: Compare the values
        if firstValue != secondValue:
            differenceCount += 1  # Increment if they differ
            
    # Step 6: Check the difference count and print result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main guard to execute the function
if __name__ == "__main__":
    doMain()
