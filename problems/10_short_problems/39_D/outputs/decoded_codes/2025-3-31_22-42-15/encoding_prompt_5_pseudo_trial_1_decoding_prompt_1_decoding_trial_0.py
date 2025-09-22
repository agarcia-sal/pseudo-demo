def main():
    # Read two lines of input, each containing three integers
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count the differences
    differenceCount = 0 
    
    # Loop through each element in the lists (we expect exactly three elements)
    for index in range(3):  # This goes from 0 to 2
        # Convert each string element to an integer
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1 
    
    # Check if the count of differences is less than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by executing the main function
main()
