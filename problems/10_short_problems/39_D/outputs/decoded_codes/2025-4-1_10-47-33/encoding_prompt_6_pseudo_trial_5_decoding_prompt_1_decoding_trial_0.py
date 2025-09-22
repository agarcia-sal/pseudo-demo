def main():
    # Read two lines of input, each containing three numbers separated by spaces
    firstLine = input()
    secondLine = input()

    # Split the input lines into lists of strings, representing the numbers
    firstList = firstLine.split()
    secondList = secondLine.split()

    # Initialize a counter for the number of differences
    differenceCount = 0 

    # Loop through the first three elements of each list
    for index in range(3):
        # Convert the string numbers to integers
        numFromFirstList = int(firstList[index])
        numFromSecondList = int(secondList[index])

        # Check if the numbers at the current index are different
        if numFromFirstList != numFromSecondList:
            # Increment the difference counter
            differenceCount += 1 

    # If the count of differences is less than 3, print "YES", otherwise print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
