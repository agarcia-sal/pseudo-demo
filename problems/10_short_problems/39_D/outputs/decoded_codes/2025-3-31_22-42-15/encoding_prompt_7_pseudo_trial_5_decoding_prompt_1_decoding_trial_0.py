def main():
    # Read two lines of input from the user, representing two sequences of numbers
    firstSequence = input()
    secondSequence = input()
    
    # Split the input strings into lists of numbers
    firstList = firstSequence.split()
    secondList = secondSequence.split()
    
    # Initialize a variable to count the number of differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements from strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            # Increment the count of differences
            differenceCount += 1
    
    # If the count of differences is less than 3, print "YES", else print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    main()
