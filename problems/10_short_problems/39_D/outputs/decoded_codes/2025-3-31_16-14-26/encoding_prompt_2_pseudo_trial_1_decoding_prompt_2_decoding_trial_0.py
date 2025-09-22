def doMain():
    # Step 2: Prompt for User Input
    inputString1 = input()
    inputString2 = input()

    # Step 3: Process the Input
    listOfValues1 = inputString1.split()
    listOfValues2 = inputString2.split()

    # Step 4: Initialize a Counter
    differenceCount = 0

    # Step 5: Compare Values
    for index in range(3):  # Looping from 0 to 2 (inclusive)
        valueA = int(listOfValues1[index])  # Convert to integer
        valueB = int(listOfValues2[index])  # Convert to integer
        if valueA != valueB:
            differenceCount += 1  # Increment the counter if values are different

    # Step 6: Output the Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start the Program
if __name__ == "__main__":
    doMain()
