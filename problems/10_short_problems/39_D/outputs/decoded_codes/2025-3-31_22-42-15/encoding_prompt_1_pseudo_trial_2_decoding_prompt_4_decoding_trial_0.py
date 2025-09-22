def doMain():
    # Step 2: Collect input from the user
    firstInput = input()
    secondInput = input()
    
    # Step 3: Split input strings into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Step 4: Initialize the difference counter
    differenceCount = 0
    
    # Step 5: Compare the values and count differences
    for index in range(3):  # Iterate from 0 to 2
        valueA = int(firstValues[index])  # Convert first value to integer
        valueB = int(secondValues[index])  # Convert second value to integer
        
        if valueA != valueB:  # Check for inequality
            differenceCount += 1  # Increment the difference counter
    
    # Step 6: Output the result based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Check if the script is executed directly
if __name__ == "__main__":
    doMain()
