def main():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input strings into lists of items
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # loop from 0 to 2
        # Convert the current elements to integers
        valueFromFirstLine = int(firstList[index])
        valueFromSecondLine = int(secondList[index])
        
        # Check if the elements are different
        if valueFromFirstLine != valueFromSecondLine:
            # Increase the differenceCount by 1
            differenceCount += 1 

    # Check the number of differences and provide output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main()
