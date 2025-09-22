def main():
    # Read input values for the first and second list
    firstList = input()
    secondList = input()
    
    # Split the input strings into lists of values
    firstValues = firstList.split()
    secondValues = secondList.split()
    
    # Initialize a counter to track the differences
    differenceCount = 0
    
    # Loop through each element of the two lists
    for x in range(3):  # Loop from 0 to 2 inclusive
        # Convert the x-th elements to integers
        valueA = int(firstValues[x])
        valueB = int(secondValues[x])
        
        # If the two values are not equal, increment the difference counter
        if valueA != valueB:
            differenceCount += 1
    
    # Check the number of differences and output the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed
if __name__ == "__main__":
    main()
