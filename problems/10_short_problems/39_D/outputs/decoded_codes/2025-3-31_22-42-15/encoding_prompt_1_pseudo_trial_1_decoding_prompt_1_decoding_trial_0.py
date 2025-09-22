def main():
    # Read two lines of input, each containing a sequence of numbers
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0
    
    # Iterate over the range of the first three elements
    for index in range(3):
        # Convert the corresponding elements from the lists to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If the numbers at this index are not equal
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1

    # After completing the comparisons, check how many differences were found
    if differenceCount < 3:
        # If there are fewer than 3 differences, print "YES"
        print("YES")
    else:
        # If there are 3 or more differences, print "NO"
        print("NO")

# Execute the main function if this script is being run as the main program
if __name__ == "__main__":
    main()
