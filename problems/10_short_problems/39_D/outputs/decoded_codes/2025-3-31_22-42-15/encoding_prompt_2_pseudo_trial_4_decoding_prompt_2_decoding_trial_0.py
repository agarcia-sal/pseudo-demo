def main():
    # Prompt the user for input and store the first line of input
    firstInput = input()
    
    # Prompt the user for another input
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to track the differences
    differencesCount = 0
    
    # Loop that will repeat three times
    for i in range(3):
        # Convert elements to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if the values are different
        if firstValue != secondValue:
            differencesCount += 1
    
    # After the loop, check the count of differences
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
