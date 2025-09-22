# Start the program

def main():
    # Prompt the user for input and store the first line of input
    firstInput = input()
    # Prompt the user for another input and store it
    secondInput = input()
    
    # Split both inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differencesCount = 0
    
    # Loop through the lists for three elements
    for i in range(3):
        # Convert corresponding elements to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if values are different
        if firstValue != secondValue:
            # Increase the differences count
            differencesCount += 1
            
    # After the loop, check the differences count
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to start the program
main()
