def main():
    # Read two lines of input containing space-separated numbers
    firstSetOfNumbers = input()
    secondSetOfNumbers = input()

    # Split the input strings into lists of numbers
    individualNumbers1 = firstSetOfNumbers.split()
    individualNumbers2 = secondSetOfNumbers.split()

    # Initialize a counter for differences
    differenceCounter = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string numbers to integers for comparison
        numberFromFirstSet = int(individualNumbers1[index])
        numberFromSecondSet = int(individualNumbers2[index])

        # Check if the numbers at the current index are different
        if numberFromFirstSet != numberFromSecondSet:
            differenceCounter += 1 

    # Determine if the number of differences is less than 3
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script runs directly
if __name__ == "__main__":
    main()
