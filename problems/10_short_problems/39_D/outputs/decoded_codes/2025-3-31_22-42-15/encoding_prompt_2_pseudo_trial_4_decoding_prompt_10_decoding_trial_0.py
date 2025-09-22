def main():
    # Prompt the user for the first line of input
    firstInput = input()
    # Prompt the user for the second line of input
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the differences count
    differencesCount = 0

    # Create a loop that will repeat three times
    for i in range(3):
        # Convert the corresponding elements to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if the values are different
        if firstValue != secondValue:
            differencesCount += 1
    
    # Check if differencesCount is less than 3
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()


    1 2 3
    1 2 3
    

    1 2 3
    1 2 4
    

    1 2 3
    4 5 6
    

    100 200 300
    100 200 400
    