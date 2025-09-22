def main():
    # Read two lines of input from the user.
    firstInput = input()
    secondInput = input()
    
    # Split each input line into a list of string elements.
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences.
    differenceCount = 0 
    
    # Loop through the first three elements of each list.
    for index in range(3):  # Loop from 0 to 2 inclusive
        # Convert the string elements to integers.
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values at the current index are different.
        if firstValue != secondValue:
            # Increment the difference count.
            differenceCount += 1 
    
    # Determine if the number of differences is less than 3.
    if differenceCount < 3:
        # Print "YES" if differences are less than 3.
        print("YES")
    else:
        # Print "NO" if differences are equal to or greater than 3.
        print("NO")

# Start the program execution.
if __name__ == "__main__":
    main()
