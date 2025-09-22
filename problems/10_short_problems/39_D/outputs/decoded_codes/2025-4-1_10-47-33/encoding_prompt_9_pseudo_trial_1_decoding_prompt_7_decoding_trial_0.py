def main():
    # Get two lines of input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstNumbers = firstInput.split()  # Splitting the first input into a list of strings
    secondNumbers = secondInput.split()  # Splitting the second input into a list of strings

    # Initialize a variable to count differences
    differenceCount = 0 

    # Loop through the first three numbers in both lists
    for index in range(3):  # Looping from 0 to 2
        # Convert the string numbers to integers
        firstNumber = int(firstNumbers[index])
        secondNumber = int(secondNumbers[index])
        
        # Check if the numbers at the same index are different
        if firstNumber != secondNumber:  # Comparing the two numbers
            differenceCount += 1  # Incrementing the difference count if they are different

    # Check if the number of differences is less than 3
    if differenceCount < 3:  # If the count of differences is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Start the program
main()
