def main():
    # Get two input strings from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements at the current index to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # If the values are different, increment the difference count
        if firstValue != secondValue:
            differenceCount += 1
            
    # If the number of differences is less than 3, print "YES"; otherwise, print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
