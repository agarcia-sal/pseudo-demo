def main():
    # Read two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split each input string into a list of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If the values are different, increment the difference counter
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine the final output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
