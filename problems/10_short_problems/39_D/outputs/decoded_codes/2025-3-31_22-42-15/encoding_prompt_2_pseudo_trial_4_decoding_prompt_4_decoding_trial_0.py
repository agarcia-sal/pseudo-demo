def main():
    # Prompt the user for the first input and store it as a string
    firstInput = input()
    # Prompt the user for the second input and store it as a string
    secondInput = input()
    
    # Split both inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for the number of differences
    differencesCount = 0
    
    # Loop through three elements (assuming both lists have at least three elements)
    for i in range(3):
        # Convert the corresponding elements to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Increment differencesCount if the values are different
        if firstValue != secondValue:
            differencesCount += 1
    
    # Determine the output based on the count of differences
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
