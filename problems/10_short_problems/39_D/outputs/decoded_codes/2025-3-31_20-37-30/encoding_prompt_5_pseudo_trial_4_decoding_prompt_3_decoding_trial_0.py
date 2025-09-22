def doMain():
    # Step 2: Read inputs from the user
    firstInput = input()
    secondInput = input()

    # Step 3: Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Step 4: Initialize a counter for differences
    differenceCount = 0

    # Step 5: Compare the value pairs at each index
    for x in range(3):  # Iterate through indices 0 to 2
        firstValue = int(firstValues[x])  # Convert first value to integer
        secondValue = int(secondValues[x])  # Convert second value to integer
        
        # If the values are different, increment the counter
        if firstValue != secondValue:
            differenceCount += 1

    # Step 6: Output the result based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function when the script is run
if __name__ == "__main__":
    doMain()
