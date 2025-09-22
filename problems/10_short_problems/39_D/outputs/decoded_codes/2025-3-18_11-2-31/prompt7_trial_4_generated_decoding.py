def main():
    # Gather input values
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of string values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize the count of differences
    differenceCount = 0
    
    # Compare the elements of both lists
    for index in range(3):  # Only comparing first three elements
        # Convert the string values to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1
            
    # Evaluate the number of differences
    if differenceCount < 3:
        print("YES")  # Indicates some level of similarity
    else:
        print("NO")   # Indicates a lack of similarity

# Entry point of the program
if __name__ == "__main__":
    main()
