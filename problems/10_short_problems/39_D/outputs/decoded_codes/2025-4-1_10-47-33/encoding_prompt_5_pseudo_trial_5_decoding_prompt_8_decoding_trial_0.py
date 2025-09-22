def main():
    # Get input from the user for both sets of numbers
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of strings
    firstSet = firstInput.split()
    secondSet = secondInput.split()

    # Initialize a counter for the number of differences
    differenceCount = 0 

    # Loop through each position in the sets (there are 3 positions)
    for index in range(3):
        # Convert the current elements from strings to integers
        firstNumber = int(firstSet[index])
        secondNumber = int(secondSet[index])
        
        # Check if the numbers at the current position are different
        if firstNumber != secondNumber:
            differenceCount += 1 

    # After checking all positions, decide the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Run the main function
main()
