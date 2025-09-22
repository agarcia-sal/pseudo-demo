def main():
    # Get user input for two sets of values
    one = input()
    two = input()

    # Split the inputs into separate values
    oneVal = one.split()
    twoVal = two.split()

    # Initialize a counter for differences
    diff = 0 

    # Compare each corresponding value in the two sets
    for index in range(3):
        firstNumber = int(oneVal[index])
        secondNumber = int(twoVal[index])

        # If the numbers are different, increase the difference count
        if firstNumber != secondNumber:
            diff += 1

    # Determine if sets are similar based on the difference count
    if diff < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
