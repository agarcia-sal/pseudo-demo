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
    for index in range(3):  # Compare three pairs of values
        valueA = int(firstValues[index])
        valueB = int(secondValues[index])
        
        # Step 5: Check if the two values are different
        if valueA != valueB:
            differenceCount += 1

    # Step 6: Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start the program execution
if __name__ == "__main__":
    main()
