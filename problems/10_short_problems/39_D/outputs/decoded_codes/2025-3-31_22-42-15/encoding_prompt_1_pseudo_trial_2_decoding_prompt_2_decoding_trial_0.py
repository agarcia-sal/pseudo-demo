def doMain():
    # Step 2: Get Input Values
    firstInput = input()
    secondInput = input()
    
    # Step 3: Split Input into Lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Step 4: Set a Difference Counter
    differenceCount = 0

    # Step 5: Iterate and Count Differences
    for index in range(3):  # Looping through 0 to 2 (inclusive)
        valueA = int(firstValues[index])
        valueB = int(secondValues[index])
        if valueA != valueB:
            differenceCount += 1

    # Step 6: Decide Output Based on Count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()
