def main():
    # Step 2: Get Inputs
    firstInput = input()
    secondInput = input()

    # Step 3: Split Inputs
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 4: Initialize a Mismatch Counter
    mismatchCount = 0

    # Step 5: Compare Values
    for index in range(3):  # Compare the first three elements
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:
            mismatchCount += 1

    # Step 6: Check Mismatch Count
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute Main Function on Program Start
if __name__ == "__main__":
    main()
