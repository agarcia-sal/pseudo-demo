def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input strings into lists of integers
    firstList = list(map(int, firstLine.split()))
    secondList = list(map(int, secondLine.split()))
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):
        # Get the numbers to compare
        firstNumber = firstList[index]
        secondNumber = secondList[index]
        
        # If the numbers are not equal, increment the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # If differences are less than 3, print "YES"; otherwise print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    doMain()


   1 2 3
   1 2 3
   

   1 2 3
   1 2 4
   

   1 2 3
   4 5 6
   

   -1 -2 -3
   -1 -2 -3
   

   0 0 0
   0 0 1
   