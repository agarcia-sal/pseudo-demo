def main():
    # Prompt the user for the first line of input
    firstInput = input()
    # Prompt the user for the second line of input
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count the differences
    differencesCount = 0
    
    # Loop through the first three elements
    for i in range(3):
        # Convert the corresponding elements to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if the values are different
        if firstValue != secondValue:
            differencesCount += 1
            
    # Check if the differences count is less than 3
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
