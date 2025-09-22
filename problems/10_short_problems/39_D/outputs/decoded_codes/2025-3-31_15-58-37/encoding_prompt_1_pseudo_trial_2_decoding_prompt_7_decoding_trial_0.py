def doMain():
    # Get two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into separate components
    splitFirstInput = firstInput.split()  # Splitting the first input into a list of elements
    splitSecondInput = secondInput.split()  # Splitting the second input into a list of elements
    
    # Initialize a variable to count the number of differences
    differenceCount = 0 

    # Iterate through the first three elements of both inputs
    for index in range(3):  # Looping through the indices 0 to 2
        # Convert the current elements to integers
        firstValue = int(splitFirstInput[index])  # Converting to integer
        secondValue = int(splitSecondInput[index])  # Converting to integer
        
        # Check if the two values are different
        if firstValue != secondValue:  # Comparing the two integer values
            # Increment the count of differences
            differenceCount += 1  # Incrementing the count if values are different
            
    # If the number of differences is less than 3, print "YES", otherwise print "NO"
    if differenceCount < 3:  # Checking if differences are less than 3
        print("YES")  # Outputting "YES" if true
    else:
        print("NO")  # Outputting "NO" if false

# Main execution flow
doMain()


     1 2 3
     1 2 3
     

     1 2 3
     1 3 3
     

     1 2 3
     4 5 6
     

     1 2 3
     1 2 0
     

     1 2 3
     1 2
     