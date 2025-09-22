def main():
    # Take inputs for two sets of values from the user
    firstSet = input()
    secondSet = input()

    # Split the input strings into individual elements
    firstValues = firstSet.split()
    secondValues = secondSet.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Iterate over the first three elements of both sets
    for index in range(3):
        # Convert current elements from string to integer
        a = int(firstValues[index])
        b = int(secondValues[index])

        # Check if elements at the current index are different
        if a != b:
            # Increment differenceCount by 1 if they are different
            differenceCount += 1

    # Determine if the difference count is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when running the script
if __name__ == "__main__":
    main()
