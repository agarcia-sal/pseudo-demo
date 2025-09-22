# Start the program

def main():
    # Read input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the first input into separate elements and store them in a list called firstList
    firstList = firstInput.split()
    
    # Split the second input into separate elements and store them in a list called secondList
    secondList = secondInput.split()
    
    # Initialize a variable called differenceCount to zero
    differenceCount = 0
    
    # For each index from 0 to 2
    for index in range(3):
        # Convert the element from firstList at the current index into an integer
        firstValue = int(firstList[index])
        
        # Convert the element from secondList at the current index into an integer
        secondValue = int(secondList[index])
        
        # If firstValue is not equal to secondValue
        if firstValue != secondValue:
            # Increment differenceCount by 1
            differenceCount += 1
    
    # If differenceCount is less than 3
    if differenceCount < 3:
        # Output "YES"
        print("YES")
    else:
        # Otherwise output "NO"
        print("NO")

# Execute the main function when the program runs
main()
