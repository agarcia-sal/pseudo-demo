# Start the program.

def main():
    # Prompt the user for input and store the first line of input in a variable named firstInput.
    firstInput = input()
    
    # Prompt the user for another input and store it in a variable named secondInput.
    secondInput = input()
    
    # Split both firstInput and secondInput into lists of strings, naming them firstList and secondList respectively.
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable named differencesCount to zero, which will track how many elements differ between the two lists.
    differencesCount = 0
    
    # Create a loop that will repeat three times (for three elements).
    for i in range(3):
        # Convert the corresponding elements from firstList and secondList into integers, naming them firstValue and secondValue.
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if firstValue is not equal to secondValue. If they are different:
        if firstValue != secondValue:
            # Increase the differencesCount by one.
            differencesCount += 1
            
    # After the loop ends, check if differencesCount is less than 3.
    if differencesCount < 3:
        # If it is, print "YES".
        print("YES")
    else:
        # Otherwise, print "NO".
        print("NO")

# End the program.
