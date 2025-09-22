def doMain():
    # Step 2: Read input values and split them into lists
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 3: Initialize the counter for differences
    differenceCount = 0

    # Step 4: Comparison Loop to count differences
    for index in range(3):  # Loop over the first three indices
        valueA = int(firstList[index])   # Convert first list value to integer
        valueB = int(secondList[index])   # Convert second list value to integer

        # Check if the values are not equal
        if valueA != valueB:
            differenceCount += 1  # Increment counter if they differ

    # Step 5: Decision making based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()


   1 2 3
   1 2 3
   

   1 2 3
   1 2 4
   

   1 2 3
   4 5 6
   

   7 8 9
   7 8 9
   