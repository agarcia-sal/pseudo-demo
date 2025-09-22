def main():
    # Receive two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split each input into a list of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0

    # Loop through each corresponding pair in the two lists
    for index in range(3):
        # Convert the string at the current index to an integer for both lists
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1

    # After comparing all three values, check the count of differences
    if differenceCount < 3:
        print("YES")  # Output that the values are similar
    else:
        print("NO")   # Output that the values are different

# Execute main function if this file is the main program
if __name__ == "__main__":
    main()
