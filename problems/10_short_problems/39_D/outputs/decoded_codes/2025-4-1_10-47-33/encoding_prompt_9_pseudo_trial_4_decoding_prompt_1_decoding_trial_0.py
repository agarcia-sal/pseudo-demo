def main():
    # Receive input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter to track position differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert each string in the lists to an integer for comparison
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # If the numbers are not equal, increment the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # Check if the difference count is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()
