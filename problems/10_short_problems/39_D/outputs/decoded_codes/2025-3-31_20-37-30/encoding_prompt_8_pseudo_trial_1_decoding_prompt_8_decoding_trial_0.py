def main():
    # Prompt the user for input values
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differencesCount = 0  # Initialize a counter for differences

    # Loop through the first three numbers in both lists
    for index in range(3):
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differencesCount += 1
            
    # Check the number of differences found
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
