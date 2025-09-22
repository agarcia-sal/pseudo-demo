def main():
    # Read two lines of input, each containing three integers
    firstInput = input()  # User inputs the first set of integers
    secondInput = input()  # User inputs the second set of integers
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()  # Split the first input into components
    secondList = secondInput.split()  # Split the second input into components
    
    # Initialize a variable to count the differences
    differenceCount = 0 
    
    # Loop through each element in the lists (we expect exactly three elements)
    for index in range(3):  # We loop through indices 0, 1, and 2
        # Convert each string element to an integer
        firstValue = int(firstList[index])  # Convert to integer from first list
        secondValue = int(secondList[index])  # Convert to integer from second list
        
        # Check if the values are different
        if firstValue != secondValue:  # Check for inequality
            # Increment the difference count
            differenceCount += 1  # Count the difference
            
    # Check if the count of differences is less than three
    if differenceCount < 3:  # Evaluate the count of differences
        print("YES")  # If fewer than three differences, output YES
    else:
        print("NO")  # Otherwise, output NO

# Start the program by executing the main function
main()
