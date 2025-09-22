# Define Main Function
def main():
    # Receive Input
    firstInput = input()
    secondInput = input()

    # Split Inputs
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize Difference Counter
    differenceCount = 0

    # Compare Corresponding Elements
    for i in range(3):  # Loop from 0 to 2 inclusive
        firstValue = int(firstList[i])      # Convert string to integer
        secondValue = int(secondList[i])    # Convert string to integer
        if firstValue != secondValue:
            differenceCount += 1  # Increment the counter

    # Determine Output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute Main Function
if __name__ == "__main__":
    main()
