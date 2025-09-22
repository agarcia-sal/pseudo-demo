def main():
    # Step 1: Accept input for two sequences
    print("Enter first sequence of three integers:")
    firstSequence = input()
    print("Enter second sequence of three integers:")
    secondSequence = input()

    # Step 2: Split the input strings into lists of integers
    firstList = firstSequence.split()
    secondList = secondSequence.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare integers in both lists
    for index in range(3):
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        # Step 5: If numbers are different, increment the counter
        if firstNumber != secondNumber:
            differenceCount += 1 

    # Step 6: Determine if the difference count is less than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute
main()
