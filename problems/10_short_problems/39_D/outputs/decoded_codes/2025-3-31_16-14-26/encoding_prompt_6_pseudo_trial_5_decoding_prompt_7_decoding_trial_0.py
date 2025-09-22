def main():
    # Read two lines of input
    firstLine = input()
    secondLine = input()

    # Split the input lines into separate values, removing any leading/trailing whitespace
    firstValues = firstLine.split()
    secondValues = secondLine.split()

    # Initialize a counter to track differences
    differenceCount = 0 

    # Iterate through the first three values of both inputs
    for index in range(3):
        # Convert the current values from strings to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increase the difference counter
            differenceCount += 1 

    # If there are fewer than three differences, print "YES", otherwise print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the main function if this script is executed
if __name__ == "__main__":
    main()
