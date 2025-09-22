def main():
    # Prompt user for input and store in variables
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differencesCount = 0
    
    # Loop through three elements to compare
    for i in range(3):
        # Convert corresponding elements to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if values are different
        if firstValue != secondValue:
            differencesCount += 1
    
    # Check the count of differences and print result
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to run the program
main()
