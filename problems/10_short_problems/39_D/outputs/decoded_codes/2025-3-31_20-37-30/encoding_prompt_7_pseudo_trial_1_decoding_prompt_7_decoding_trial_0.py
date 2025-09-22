def main():
    # Read two lines of input representing two sets of data
    firstSet = input()
    secondSet = input()
    
    # Split the input data into individual components
    firstComponents = firstSet.split()
    secondComponents = secondSet.split()
    
    # Initialize a counter to track differences
    differenceCount = 0
    
    # Iterate through the first three components
    for index in range(3):
        # Convert the components from strings to integers
        firstValue = int(firstComponents[index])
        secondValue = int(secondComponents[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter if they are different
            differenceCount += 1
            
    # Evaluate the total number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution starts here
main()
