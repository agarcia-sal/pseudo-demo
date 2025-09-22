def doMain():
    # Step 2: Read Values
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 3: Initialize Counter
    differenceCount = 0
    
    # Step 4: Check Values
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        valueA = int(firstList[index])      # Convert to integer
        valueB = int(secondList[index])     # Convert to integer
        
        if valueA != valueB:  # Check if values are different
            differenceCount += 1  # Increment counter

    # Step 5: Output Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Execute the Main Function
if __name__ == "__main__":
    doMain()
