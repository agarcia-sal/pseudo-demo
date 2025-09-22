def main():
    # Step 1: Read two lines of input
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a variable to count differences
    differenceCount = 0 

    # Step 4: Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Step 5: Check for differences between the elements
        if firstValue != secondValue:
            differenceCount += 1 

    # Step 6: Check the count of differences to decide output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Check if this file is executed as main
if __name__ == "__main__":
    main()
