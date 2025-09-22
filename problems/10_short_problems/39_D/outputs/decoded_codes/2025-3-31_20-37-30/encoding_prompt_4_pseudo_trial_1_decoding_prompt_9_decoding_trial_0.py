def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of string elements
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert strings to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the elements are different
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine the output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    doMain()
