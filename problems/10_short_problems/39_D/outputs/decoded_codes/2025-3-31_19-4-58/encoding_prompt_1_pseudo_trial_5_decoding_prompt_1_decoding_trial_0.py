def main():
    # Input
    firstList = input()
    secondList = input()
    
    # Process the inputs
    firstValues = firstList.split()
    secondValues = secondList.split()

    # Initialize a counter
    differenceCount = 0

    # Loop through each element in the range of 0 to 2 (inclusive)
    for x in range(3):
        valueA = int(firstValues[x])
        valueB = int(secondValues[x])

        # Check for differences
        if valueA != valueB:
            differenceCount += 1

    # Check the value of differenceCount
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed
if __name__ == "__main__":
    main()
