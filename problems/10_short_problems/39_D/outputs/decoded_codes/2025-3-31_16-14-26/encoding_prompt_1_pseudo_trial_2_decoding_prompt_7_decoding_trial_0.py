def main():
    # Step 1: Get input
    firstInput = input()  # Read first input
    secondInput = input()  # Read second input

    # Step 2: Split the inputs into lists of strings
    firstList = firstInput.split()  # Split first input using spaces
    secondList = secondInput.split()  # Split second input using spaces

    # Initialize a counter to track differences
    differenceCount = 0  # Start with zero differences

    # Step 3: Compare corresponding elements of the two lists
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        # Convert string elements to integers
        valueFromFirstList = int(firstList[index])  # Convert to integer
        valueFromSecondList = int(secondList[index])  # Convert to integer
        
        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:  # Compare values
            differenceCount += 1  # Increment count if different

    # Step 4: Check the number of differences
    if differenceCount < 3:  # Check if differences are less than 3
        print("YES")  # Print YES if fewer than 3 differences
    else: 
        print("NO")  # Print NO otherwise

# Invoke the main function when running the program
main()  # Call main to execute
