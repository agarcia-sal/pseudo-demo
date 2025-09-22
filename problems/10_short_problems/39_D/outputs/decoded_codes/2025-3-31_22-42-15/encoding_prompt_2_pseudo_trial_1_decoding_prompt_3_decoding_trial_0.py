def main():
    # Step 2: Prompt the user to input the first set of values
    firstInput = input()
    
    # Step 3: Prompt the user to input the second set of values
    secondInput = input()
    
    # Step 4: Split the first input string into a list of values
    firstValues = firstInput.split()
    
    # Step 5: Split the second input string into a list of values
    secondValues = secondInput.split()
    
    # Step 6: Initialize a counter for differences
    differenceCount = 0
    
    # Step 7: Compare the corresponding values in the two sets
    for index in range(3):  # Loop over the first three indices (0 to 2)
        firstValue = int(firstValues[index])  # Convert to integer
        secondValue = int(secondValues[index])  # Convert to integer
        
        # If the values are not equal, increment the difference count
        if firstValue != secondValue:
            differenceCount += 1
            
    # Step 8: Check the difference count to determine the output
    if differenceCount < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Step 9: Execute the main process
if __name__ == "__main__":
    main()
