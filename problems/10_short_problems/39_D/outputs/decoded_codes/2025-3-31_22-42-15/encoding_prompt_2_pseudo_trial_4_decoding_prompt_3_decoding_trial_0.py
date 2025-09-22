def main():
    # Prompt the user for input and store them in variables
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize differencesCount to track differing elements
    differencesCount = 0
    
    # Loop through the elements of both lists, checking for differences
    for i in range(3):  # Assuming both lists have at least 3 elements
        firstValue = int(firstList[i])  # Convert to integer
        secondValue = int(secondList[i])  # Convert to integer
        
        # Increment the differencesCount if the values are different
        if firstValue != secondValue:
            differencesCount += 1
            
    # Print "YES" if differencesCount is less than 3, else print "NO"
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
