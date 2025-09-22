# Function Definition: Start Main Function
def doMain():
    # Input Collection: Get Input Values
    firstInput = input()
    secondInput = input()
    
    # Data Preparation: Split Input into Lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize Counter: Set a Difference Counter
    differenceCount = 0
    
    # Comparison Loop: Iterate and Count Differences
    for index in range(3):  # Iterate from 0 to 2
        valueA = int(firstValues[index])   # Convert value from firstValues to integer
        valueB = int(secondValues[index])  # Convert value from secondValues to integer
        
        if valueA != valueB:  # Check for inequality
            differenceCount += 1  # Increase the count if values are different
    
    # Conditional Check: Decide Output Based on Count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Program Execution: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()  # Call the main function to start the process
