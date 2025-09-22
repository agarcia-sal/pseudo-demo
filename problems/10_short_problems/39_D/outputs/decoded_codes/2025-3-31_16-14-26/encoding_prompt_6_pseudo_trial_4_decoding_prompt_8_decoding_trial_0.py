def main():
    # Get inputs from the user
    firstString = input()
    secondString = input()
    
    # Split the input strings into lists of strings
    firstList = firstString.split()
    secondList = secondString.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            # Increment the difference counter
            differenceCount += 1
            
    # Check the number of differences found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
