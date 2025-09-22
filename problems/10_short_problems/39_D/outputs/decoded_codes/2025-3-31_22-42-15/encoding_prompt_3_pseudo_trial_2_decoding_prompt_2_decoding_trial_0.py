def main():
    # Step 1: Collect input
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into separate components
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare elements from both lists
    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Step 5: Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1 

    # Step 6: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function if this script is run
if __name__ == "__main__":
    main()
