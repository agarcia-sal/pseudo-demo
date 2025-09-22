def main():
    # Get two lines of input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstNumbers = firstInput.split()
    secondNumbers = secondInput.split()

    # Initialize a variable to count differences
    differenceCount = 0 

    # Loop through the first three numbers in both lists
    for index in range(3):
        # Convert the string numbers to integers
        firstNumber = int(firstNumbers[index])
        secondNumber = int(secondNumbers[index])
        
        # Check if the numbers at the same index are different
        if firstNumber != secondNumber:
            differenceCount += 1

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
