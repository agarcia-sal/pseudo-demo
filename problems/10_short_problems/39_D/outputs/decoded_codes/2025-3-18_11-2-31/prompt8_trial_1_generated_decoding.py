def main():
    # Step 1: Read two lines of input
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into a list of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a count for differences
    differenceCount = 0 

    # Step 4: Compare each corresponding number from both lists
    for index in range(3):  # loop through the indices 0 to 2
        # Convert the elements from strings to integers
        numberFromFirstList = int(firstList[index])
        numberFromSecondList = int(secondList[index])

        # If the numbers are not equal, increase the difference count
        if numberFromFirstList != numberFromSecondList:
            differenceCount += 1

    # Step 5: Evaluate the number of differences to determine the output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
