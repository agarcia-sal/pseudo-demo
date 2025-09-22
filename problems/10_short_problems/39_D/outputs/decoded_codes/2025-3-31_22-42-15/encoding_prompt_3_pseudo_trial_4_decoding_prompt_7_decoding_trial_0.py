def doMain():
    # Read two input strings from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of substrings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differing elements
    differenceCount = 0 

    # Iterate over the indices for the lists (assuming they both have 3 elements)
    for index in range(3):  # Indexing from 0 to 2
        # Convert the elements to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Compare the corresponding elements
        if firstNumber != secondNumber:
            # Increment the counter if they are different
            differenceCount += 1

    # Check how many elements differ
    if differenceCount < 3:
        print("YES")  # Output "YES" if less than 3 differences
    else:
        print("NO")   # Output "NO" if 3 or more differences

# Main execution begins here
if __name__ == "__main__":
    doMain()
