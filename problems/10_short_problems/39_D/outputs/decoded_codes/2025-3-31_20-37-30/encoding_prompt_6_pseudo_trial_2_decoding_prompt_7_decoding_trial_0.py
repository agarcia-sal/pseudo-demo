def main():
    # Read input strings from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of words
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCounter = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values from both lists are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCounter += 1 
    
    # After comparing all three values, check the difference counter
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Trigger the main function when the program starts
main()
