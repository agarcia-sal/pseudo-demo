# Start the program

def main():
    # Prompt for user input
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input

    # Process the inputs
    firstList = firstInput.split()  # Split firstInput into a list of strings
    secondList = secondInput.split()  # Split secondInput into a list of strings

    # Initialize a counter
    differenceCount = 0  # Set a variable to zero

    # Compare the elements of both lists
    for index in range(3):  # For each index from 0 to 2
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        if firstValue != secondValue:  # If they are not equal
            differenceCount += 1  # Increment the counter

    # Decide the result based on the count of differences
    if differenceCount < 3:  # If less than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# If this file is executed as the main program
if __name__ == "__main__":
    main()  # Call the main function
