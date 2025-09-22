def compareInputsAndDetermineResult():
    # Prompt the user for the first input string
    firstInput = input()
    
    # Prompt the user for the second input string
    secondInput = input()
    
    # Split the input strings into lists of numbers
    firstList = list(map(int, firstInput.split()))
    secondList = list(map(int, secondInput.split()))
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding positions in the two lists
    for position in range(3):
        firstNumber = firstList[position]
        secondNumber = secondList[position]
        
        # If the numbers do not match, increase the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1
            
    # Check the total number of differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences means the sequences are similar enough
    else:
        print("NO")   # 3 or more differences indicate significant divergence

# Main execution starts here
if __name__ == "__main__":
    compareInputsAndDetermineResult()
