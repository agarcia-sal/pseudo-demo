# Start Program
def main():
    # Receive Input
    firstList = input()  # Read a string from the user
    secondList = input()  # Read a second string from the user

    # Split Input into Lists
    firstElements = firstList.split()  # Divide firstList into elements
    secondElements = secondList.split()  # Divide secondList into elements

    # Initialize a Counter
    differenceCount = 0  # Create a variable for counting differences

    # Compare Corresponding Elements
    for index in range(3):  # Loop through indices from 0 to 2
        currentFirstValue = int(firstElements[index])  # Convert to integer
        currentSecondValue = int(secondElements[index])  # Convert to integer
        
        if currentFirstValue != currentSecondValue:  # Compare values
            differenceCount += 1  # Increase differenceCount if they are different

    # Check Number of Differences
    if differenceCount < 3:  # Check if differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Invoke Main Function to Begin Execution
main()
# End Program
