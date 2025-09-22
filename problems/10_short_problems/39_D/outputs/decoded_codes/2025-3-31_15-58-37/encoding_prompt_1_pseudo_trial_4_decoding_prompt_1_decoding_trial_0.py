def main():
    # Read two input strings from the user
    firstInputString = input()
    secondInputString = input()
    
    # Split the input strings into lists of substrings
    firstList = firstInputString.split()
    secondList = secondInputString.split()
    
    # Initialize a variable to count the number of differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1 
    
    # Determine the output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
