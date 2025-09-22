# Start the program

def main():  # Define the main function
    firstInput = input()  # Read input from the user
    secondInput = input()  # Read input from the user
    
    firstList = firstInput.split()  # Split the first input into separate elements and store them in a list
    secondList = secondInput.split()  # Split the second input into separate elements and store them in a list
    
    differenceCount = 0  # Initialize a variable called differenceCount to zero
    
    for index in range(3):  # For each index from 0 to 2
        firstValue = int(firstList[index])  # Convert the element from firstList at the current index into an integer
        secondValue = int(secondList[index])  # Convert the element from secondList at the current index into an integer
        
        if firstValue != secondValue:  # If firstValue is not equal to secondValue
            differenceCount += 1  # Increment differenceCount by 1
    
    if differenceCount < 3:  # If differenceCount is less than 3
        print("YES")  # Output "YES"
    else:  # Otherwise
        print("NO")  # Output "NO"

# Execute the main function when the program runs
main()
