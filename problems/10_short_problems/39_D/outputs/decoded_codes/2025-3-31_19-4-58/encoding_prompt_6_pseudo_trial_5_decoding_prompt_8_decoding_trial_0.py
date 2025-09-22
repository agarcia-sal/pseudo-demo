def Main():
    # Read two input strings from the user
    firstString = input()
    secondString = input()

    # Split the input strings into a list of values
    valuesFromFirstString = firstString.split()
    valuesFromSecondString = secondString.split()

    # Initialize a counter to track differences
    differenceCount = 0 

    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers
        valueFromFirst = int(valuesFromFirstString[index])
        valueFromSecond = int(valuesFromSecondString[index])

        # Check if the two values are different
        if valueFromFirst != valueFromSecond:
            # Increment the difference counter
            differenceCount += 1 

    # If the count of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Output confirms that the two sets are similar
    else:
        print("NO")   # Output indicates significant differences

# Main execution point of the program
if __name__ == "__main__":
    Main()
