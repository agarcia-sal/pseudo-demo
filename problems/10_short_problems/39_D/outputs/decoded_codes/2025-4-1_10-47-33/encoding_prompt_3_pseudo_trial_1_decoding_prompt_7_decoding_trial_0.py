def doMain():
    # Read input values for two test cases
    firstTestCase = input()
    secondTestCase = input()
    
    # Split the input strings into lists of strings
    firstTestList = firstTestCase.split()  # Split on whitespace
    secondTestList = secondTestCase.split()  # Split on whitespace

    # Initialize count of differences
    differenceCount = 0

    # Compare corresponding elements of both test cases
    for index in range(3):  # We assume the input will always have 3 elements to compare
        # Convert the string values to integers
        valueFromFirstTest = int(firstTestList[index])
        valueFromSecondTest = int(secondTestList[index])
        
        # Check if the values from both test cases are different
        if valueFromFirstTest != valueFromSecondTest:
            differenceCount += 1  # Increment the count if values are different

    # Decide if the number of differences is acceptable
    if differenceCount < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
