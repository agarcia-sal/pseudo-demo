def main():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into separate values
    firstValues = firstLine.split()
    secondValues = secondLine.split()
    
    # Initialize a variable to count differences
    differenceCount = 0 
    
    # Compare corresponding values from both lists
    for index in range(3):  # Loop from 0 to 2
        firstValue = int(firstValues[index])  # Convert to integer
        secondValue = int(secondValues[index])  # Convert to integer
        
        # Check for inequality between the two values
        if firstValue != secondValue:
            differenceCount += 1  # Increase count by 1
    
    # Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the main function
main()
