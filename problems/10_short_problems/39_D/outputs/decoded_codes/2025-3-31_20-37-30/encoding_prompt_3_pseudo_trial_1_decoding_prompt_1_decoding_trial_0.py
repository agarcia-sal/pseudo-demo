def main():
    # Prompt user for two inputs
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of values
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the current values are different
        if firstValue != secondValue:
            differenceCount += 1
    
    # Decide the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start program execution
main()
