def main():
    # Step 2: Get Inputs
    firstInput = input()  # Prompt user for the first input
    secondInput = input()  # Prompt user for the second input
    
    # Step 3: Split Inputs
    firstList = firstInput.split()  # Split first input into a list of strings
    secondList = secondInput.split()  # Split second input into a list of strings
    
    # Step 4: Initialize a Mismatch Counter
    mismatchCount = 0  # Variable to count mismatches
    
    # Step 5: Compare Values
    for i in range(3):  # Iterate over the first three indices
        firstValue = int(firstList[i])  # Convert from string to integer
        secondValue = int(secondList[i])  # Convert from string to integer
        if firstValue != secondValue:  # Check for mismatch
            mismatchCount += 1  # Increment mismatch count if values are different
    
    # Step 6: Check Mismatch Count
    if mismatchCount < 3:  # If less than 3 mismatches
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 8: Execute Main Function on Program Start
if __name__ == "__main__":
    main()
