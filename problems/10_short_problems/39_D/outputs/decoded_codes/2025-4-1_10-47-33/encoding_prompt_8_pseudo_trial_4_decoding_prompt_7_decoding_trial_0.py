def userInput():
    # Return input from the user
    return input()

def split(inputString):
    # Return a list of words from the inputString
    return inputString.split()

def convert(stringValue):
    # Return the integer value of stringValue
    return int(stringValue)

def main():
    # Read two lines of input from the user, representing two sets of numbers
    firstInput = userInput()
    secondInput = userInput()

    # Split the input strings into lists of numbers
    numbersFromFirstInput = split(firstInput)
    numbersFromSecondInput = split(secondInput)

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the first three numbers from both inputs
    for index in range(3):
        # Convert the current number from the first input to an integer
        numberFromFirstInput = convert(numbersFromFirstInput[index])
        
        # Convert the current number from the second input to an integer
        numberFromSecondInput = convert(numbersFromSecondInput[index])
        
        # Check if the numbers from both inputs are different
        if numberFromFirstInput != numberFromSecondInput:
            # Increment the difference counter
            differenceCount += 1

    # Evaluate the total number of differences
    if differenceCount < 3:
        # Output "YES" if there are fewer than three differences
        print("YES")
    else:
        # Output "NO" if there are three or more differences
        print("NO")

# Run the main function
main()
