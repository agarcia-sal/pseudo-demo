def main():
    # Read two lines of input, representing two sets of values
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers for comparison
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])
        
        # Check if the values are different
        if valueFromFirst != valueFromSecond:
            # Increment the difference counter
            differenceCount += 1
    
    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()
