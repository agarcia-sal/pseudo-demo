def main():
    # Step 1: Read two lines of input from the user
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into lists of substrings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare elements from both lists
    for index in range(3):
        # Convert the current elements to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Count how many values are different
        if firstValue != secondValue:
            differenceCount += 1

    # Step 5: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to run the program
main()
