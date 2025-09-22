def main():
    # Read input values
    firstInput = input()
    secondInput = input()

    # Split the input strings into separate integer components
    firstList = list(map(int, firstInput.split()))
    secondList = list(map(int, secondInput.split()))

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the three integers
    for index in range(3):
        firstValue = firstList[index] 
        secondValue = secondList[index] 
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1

    # Determine if the number of differences is less than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
