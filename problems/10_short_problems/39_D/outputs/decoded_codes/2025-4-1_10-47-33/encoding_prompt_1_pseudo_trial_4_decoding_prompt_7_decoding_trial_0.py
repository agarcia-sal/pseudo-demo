def main():
    # Prompt user for input and store in variables
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the difference counter
    differenceCount = 0

    # Compare the elements of both lists for the first three elements
    for index in range(3):  # Loop through indices 0, 1, 2
        # Convert string elements to integers for comparison
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])

        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:
            # Increment the difference count if they are not equal
            differenceCount += 1

    # Evaluate how many differences were found and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
