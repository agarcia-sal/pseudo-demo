def main():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()
    
    # Split the input strings into lists of values
    firstValues = firstLine.split()
    secondValues = secondLine.split()
    
    # Initialize a counter for the number of differences
    differenceCount = 0 
    
    # Loop through each position of the three values
    for index in range(3):
        # Convert values from strings to integers for comparison
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the current values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1
            
    # Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
