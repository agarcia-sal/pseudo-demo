def main():
    # Read two lines of input
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists
    firstTriplet = firstInput.split()
    secondTriplet = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both triplets
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstTriplet[index])
        secondValue = int(secondTriplet[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment differenceCount by 1
            differenceCount += 1
            
    # Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()
