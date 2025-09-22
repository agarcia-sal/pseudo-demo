def main():
    # Read two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the two numbers are different
        if firstNumber != secondNumber:
            # Increment the counter for differences
            differenceCount += 1
    
    # Check if the total differences are less than three
    if differenceCount < 3:
        print("YES")  # Fewer than three differences
    else:
        print("NO")   # Three or more differences

# Main entry point of the program
if __name__ == "__main__":
    main()


     1 2 3
     1 2 3
     

     YES
     

     1 2 3
     1 2 4
     

     YES
     

     1 2 3
     0 2 4
     

     YES
     

     1 2 3
     4 5 6
     

     NO
     

     -1 -2 -3
     -1 -2 -4
     

     YES
     