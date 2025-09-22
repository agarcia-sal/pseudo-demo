def main():
    # Read inputs for two lines of numbers
    firstLine = input()
    secondLine = input()

    # Split the input strings into lists of numbers
    firstNumbers = firstLine.split()
    secondNumbers = secondLine.split()
    
    # Initialize a counter to track differences
    differenceCount = 0 

    # Iterate over the first three elements of the lists
    for index in range(3):
        # Convert the string numbers to integers
        numberFromFirstLine = int(firstNumbers[index])
        numberFromSecondLine = int(secondNumbers[index])

        # Check if the numbers are different
        if numberFromFirstLine != numberFromSecondLine:
            # Increment the difference counter if they are not equal
            differenceCount += 1 

    # If the count of differences is less than 3, print "YES"
    if differenceCount < 3:
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
