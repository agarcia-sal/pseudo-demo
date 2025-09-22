def main():
    # Read two input strings from the user
    firstString = input()
    secondString = input()

    # Split the input strings into lists of substrings
    firstTuple = firstString.split()
    secondTuple = secondString.split()
    
    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstTuple[index])
        secondValue = int(secondTuple[index])

        # Check if the current elements are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1

    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
