def main():
    # Read the first line of input, which contains a set of three integers
    firstInputLine = input()
    # Read the second line of input, which contains another set of three integers
    secondInputLine = input()

    # Split the input lines into individual string components
    firstSet = firstInputLine.split()
    secondSet = secondInputLine.split()

    # Initialize a counter to track the number of mismatches
    mismatchCount = 0 

    # Iterate through each index from 0 to 2 (for three comparisons)
    for index in range(3):
        # Convert the string values to integers for comparison
        firstValue = int(firstSet[index])
        secondValue = int(secondSet[index])
        
        # Check if the two values are different
        if firstValue != secondValue:
            # Increment the mismatch counter
            mismatchCount += 1 

    # Check if the number of mismatches is less than 3
    if mismatchCount < 3:
        # If there are fewer than 3 mismatches, print "YES"
        print("YES")
    else:
        # If there are 3 or more mismatches, print "NO"
        print("NO")

# Start execution of the program by calling the main function
main()
