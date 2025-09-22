def main():
    # Get two input strings
    firstString = input()
    secondString = input()

    # Split the input strings into lists of strings
    firstValues = firstString.split()
    secondValues = secondString.split()

    # Initialize a counter to track differences
    differenceCount = 0

    # Loop through each position in the lists (assuming they have exactly 3 elements)
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])

        # Compare the two values
        if firstValue != secondValue:
            # Increment the difference count if they are not equal
            differenceCount += 1

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()
