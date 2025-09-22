# Start Program

# Define Main Function
def main():
    # Receive Input
    firstList = input()  # Read first list of values
    secondList = input()  # Read second list of values
    
    # Split Input into Lists
    firstElements = firstList.split()  # Split firstList into elements
    secondElements = secondList.split()  # Split secondList into elements
    
    # Initialize a Counter
    differenceCount = 0  # Counter for differences
    
    # Compare Corresponding Elements
    for index in range(3):  # Loop over the first three elements
        currentFirstValue = int(firstElements[index])  # Convert first element to integer
        currentSecondValue = int(secondElements[index])  # Convert second element to integer
        
        # Check if current values are different
        if currentFirstValue != currentSecondValue:
            differenceCount += 1  # Increase counter if values are different
    
    # Check Number of Differences
    if differenceCount < 3:
        print("YES")  # Output "YES" if fewer than 3 differences
    else:
        print("NO")  # Output "NO" if 3 or more differences

# Invoke Main Function to Begin Execution
main()

# End Program
