def main():
    # Accept input for two sequences of numbers
    firstSequence = input()
    secondSequence = input()
    
    # Split the input sequences into lists of numbers
    firstList = firstSequence.split()
    secondList = secondSequence.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Iterate over the range of the list indices (0 to 2, inclusive)
    for index in range(3):
        # Convert the elements at the current index to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Compare the two numbers
        if firstNumber != secondNumber:
            # Increment the counter if they are different
            differenceCount += 1 

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        # Print "YES" if fewer than 3 differences are found
        print("YES")
    else:
        # Print "NO" if 3 or more differences are found
        print("NO")

# Execute the main function as the starting point of the program
main()
