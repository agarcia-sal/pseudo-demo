def main():
    # Step 1: Obtain inputs from the user
    firstInput = input()
    secondInput = input()
    
    # Step 2: Split the input strings into lists of individual string values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Step 3: Initialize a counter for differences
    differenceCount = 0
    
    # Step 4: Compare the values in the two lists
    for index in range(3):  # since we want to compare three pairs of values
        valueA = int(firstValues[index])  # Convert to integer
        valueB = int(secondValues[index])  # Convert to integer
        
        # Step 5: Check if the two values are different
        if valueA != valueB:
            differenceCount += 1  # Increment counter
    
    # Step 6: Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")  # Output YES
    else:
        print("NO")   # Output NO

# Step 7: Start the program execution
if __name__ == "__main__":
    main()
