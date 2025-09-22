def main():
    # Prompt the user for two sets of numbers
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Compare corresponding elements from both lists
    for index in range(3):  # Looping from 0 to 2 (three elements)
        # Convert the current elements to integers for comparison
        numberFromFirstList = int(firstList[index])
        numberFromSecondList = int(secondList[index])

        # Check if the numbers are different
        if numberFromFirstList != numberFromSecondList:
            differenceCount += 1  # Increment difference count if elements are different

    # Evaluate the number of differences 
    if differenceCount < 3:
        print("YES")  # Output "YES" if less than three differences
    else:
        print("NO")   # Output "NO" if three or more differences

# This part indicates that the main function will run when the script is executed
if __name__ == "__main__":
    main()
