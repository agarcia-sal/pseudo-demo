def main():
    # Read two lines of input representing two sets of values
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Iterate through the first three values of both lists
    for index in range(3):
        # Convert the current values from strings to integers
        valueA = int(firstValues[index])
        valueB = int(secondValues[index])
        
        # Compare the current values
        if valueA != valueB:
            # Increment the difference counter if they are different
            differenceCount += 1
    
    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed
main()


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     4 5 3
     

     1 2 3
     4 5 6
     

     1 2
     1 2
     