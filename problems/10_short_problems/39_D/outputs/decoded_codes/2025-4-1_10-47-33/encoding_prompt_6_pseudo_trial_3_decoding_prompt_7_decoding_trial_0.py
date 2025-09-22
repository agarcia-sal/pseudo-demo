def doMain():
    # Step 1: Read input values.
    firstInput = input()  # Read the first input from the user
    secondInput = input()  # Read the second input from the user
    
    # Step 2: Split the input strings into lists of words.
    firstInputList = firstInput.split()  # Split the first input by spaces
    secondInputList = secondInput.split()  # Split the second input by spaces
    
    # Step 3: Initialize a counter for differences.
    differenceCount = 0  # Counter to track the number of differences
    
    # Step 4: Compare corresponding elements in both lists.
    for index in range(3):  # Assuming we are only comparing the first 3 elements
        # Convert string elements to integers for comparison.
        valueFromFirstList = int(firstInputList[index])  # Convert element to integer
        valueFromSecondList = int(secondInputList[index])  # Convert element to integer
        
        # Check if the values are different.
        if valueFromFirstList != valueFromSecondList:  # Compare values
            differenceCount += 1  # Increment difference count if they are not equal
            
    # Step 5: Determine result based on the number of differences.
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Otherwise, print NO

# Main execution block.
if __name__ == "__main__":  # Ensure the function is called only when the script runs directly
    doMain()
