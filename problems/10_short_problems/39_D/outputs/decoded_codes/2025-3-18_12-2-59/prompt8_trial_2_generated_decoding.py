def main():
    # Read two lines of integers from user input
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Iterate over each element in the lists (from index 0 to 2)
    for index in range(3):
        # Convert the string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the two integer values are different
        if firstValue != secondValue:
            # Increase the difference count
            differenceCount += 1 
    
    # If the number of differences is less than 3, print "YES"; otherwise, print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
