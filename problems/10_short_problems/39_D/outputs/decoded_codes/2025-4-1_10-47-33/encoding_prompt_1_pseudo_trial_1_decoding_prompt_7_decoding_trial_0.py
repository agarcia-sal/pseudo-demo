def MainProcedure():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of strings
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current element from each list to an integer
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])
        
        # Check if the two values are different
        if valueFromFirstList != valueFromSecondList:
            # Increment the difference counter
            differenceCount += 1

    # Check the total number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    MainProcedure()
