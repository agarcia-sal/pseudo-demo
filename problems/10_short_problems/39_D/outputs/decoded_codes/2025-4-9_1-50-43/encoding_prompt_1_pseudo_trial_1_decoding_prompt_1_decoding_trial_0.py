def main():
    # Read the first input line from the user
    firstInput = input()
    # Read the second input line from the user
    secondInput = input()

    # Split the inputs into lists of strings
    firstInputList = firstInput.split()
    secondInputList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through each of the three elements
    for index in range(3):
        # Convert the current elements to integers
        firstNumber = int(firstInputList[index])
        secondNumber = int(secondInputList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            # Increment the difference counter
            differenceCount += 1 

    # Check the count of differences
    if differenceCount < 3:
        # If differences are fewer than 3, print "YES"
        print("YES")
    else:
        # If differences are 3 or more, print "NO"
        print("NO")

# Start the program by calling the main function
main()
