def main():
    # Prompt for user input
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input

    # Process the inputs
    firstList = firstInput.split()  # Split the first input into a list of strings
    secondList = secondInput.split()  # Split the second input into a list of strings

    # Initialize a counter
    differenceCount = 0  # To keep track of differences

    # Compare the elements of both lists
    for index in range(3):  # We know we will compare 3 elements
        firstValue = int(firstList[index])  # Convert element to an integer
        secondValue = int(secondList[index])  # Convert element to an integer
        if firstValue != secondValue:  # Check for differences
            differenceCount += 1  # Increment counter if values are different

    # Decide the result based on the count of differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

if __name__ == "__main__":
    main()  # Call the main function if the file is executed
