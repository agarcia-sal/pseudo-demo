def main():
    # Read input values for two sets of data
    firstString = input()
    secondString = input()

    # Split the input strings into lists of values
    firstValues = firstString.split()
    secondValues = secondString.split()

    # Initialize a counter to track differences
    differenceCount = 0 

    # Compare the corresponding values in the two lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the string values to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the two values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment counter by 1

    # Determine if the count of differences warrants a "YES" or "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
main()
