def Main():
    # Step 1: Get user input
    firstInput = input()   # Read first line of input
    secondInput = input()  # Read second line of input

    # Step 2: Split inputs into lists of strings
    firstList = firstInput.split()   # Split firstInput into a list of strings
    secondList = secondInput.split()  # Split secondInput into a list of strings

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # Loop through indices 0 to 2
        firstValue = int(firstList[index])   # Convert string to integer
        secondValue = int(secondList[index])  # Convert string to integer
        
        if firstValue != secondValue:  # Check if values are not equal
            differenceCount += 1  # Increase difference count if values differ

    # Step 5: Determine the result based on the number of differences
    if differenceCount < 3: 
        print("YES")   # Less than 3 differences
    else:
        print("NO")    # 3 or more differences

# Step 6: Start the program execution
if __name__ == "__main__":  # Check if script is being executed directly
    Main()   # Execute the Main function
