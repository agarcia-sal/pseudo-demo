def main():
    # Read input from the user
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize the difference count
    differenceCount = 0

    # Compare values in the first and second lists
    for index in range(3):  # Loop from 0 to 2
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer

        # Increment differenceCount if values are not equal
        if firstValue != secondValue:
            differenceCount += 1

    # Output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
if __name__ == "__main__":
    main()


   1 2 3
   1 2 3
   

   5 5 5
   5 5 6
   

   10 20 30
   30 20 10
   