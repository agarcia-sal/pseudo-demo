def main():
    # Read two lines of input, representing the first and second lists of numbers.
    firstList = input()
    secondList = input()
    
    # Split the input strings into lists of values.
    firstValues = firstList.split()
    secondValues = secondList.split()
    
    # Initialize a counter for differences.
    differenceCount = 0
    
    # Loop through each of the first three elements.
    for x in range(3):
        # Convert the x-th element of both lists to integers.
        valueA = int(firstValues[x])
        valueB = int(secondValues[x])
        
        # Check if the values are different.
        if valueA != valueB:
            differenceCount += 1
    
    # Output "YES" if there are fewer than 3 differences, otherwise "NO".
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed.
if __name__ == "__main__":
    main()
