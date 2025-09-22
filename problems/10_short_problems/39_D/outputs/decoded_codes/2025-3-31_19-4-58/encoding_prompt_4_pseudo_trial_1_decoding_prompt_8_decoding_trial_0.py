def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input strings into lists of integers
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):
        # Convert string to integer for comparison
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # If the numbers are not equal, increment the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # If differences are less than 3, print "YES", otherwise print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    doMain()
