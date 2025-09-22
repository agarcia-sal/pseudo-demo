def main():
    # Prompt the user to input two sets of numbers
    print("Please enter the first set of numbers:")
    firstSet = input()
    print("Please enter the second set of numbers:")
    secondSet = input()
    
    # Split the input strings into individual numbers
    numbersFromFirstSet = firstSet.split()
    numbersFromSecondSet = secondSet.split()
    
    # Initialize a counter for differences
    differenceCounter = 0 
    
    # Loop through each pair of corresponding numbers
    for index in range(3):
        # Convert the input strings to integers
        firstNumber = int(numbersFromFirstSet[index])
        secondNumber = int(numbersFromSecondSet[index])
        
        # Compare the numbers and increment the counter if they differ
        if firstNumber != secondNumber:
            differenceCounter += 1
    
    # Check the number of differences and output the result
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
