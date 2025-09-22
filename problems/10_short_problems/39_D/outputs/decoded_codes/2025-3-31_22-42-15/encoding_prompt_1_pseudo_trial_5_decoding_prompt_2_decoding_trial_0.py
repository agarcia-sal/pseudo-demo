def main():
    # Read input values for two test cases
    testCase1 = input()
    testCase2 = input()

    # Split the input strings into lists of values
    values1 = testCase1.split()
    values2 = testCase2.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Compare corresponding elements from the two lists
    for index in range(3):  # Loop from 0 to 2 inclusive
        # Convert string values to integers
        value1 = int(values1[index])
        value2 = int(values2[index])

        # Check if the values are different
        if value1 != value2:
            differenceCount += 1  # Increment counter if values are different

    # Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
