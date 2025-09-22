def main():
    # Step 1: Receive input for the first set of integers
    print("Enter the first set of integers:")
    firstSet = input()

    # Step 2: Receive input for the second set of integers
    print("Enter the second set of integers:")
    secondSet = input()

    # Step 3: Split the input into individual integers
    firstSetList = firstSet.split()  # Split the first set string into a list of strings
    secondSetList = secondSet.split()  # Split the second set string into a list of strings

    # Step 4: Initialize a counter for differences
    differenceCount = 0

    # Step 5: Compare corresponding integers in both sets
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current string values to integers
        firstValue = int(firstSetList[index])  # Convert first set value to integer
        secondValue = int(secondSetList[index])  # Convert second set value to integer
        
        # Step 6: Check if the integers are different
        if firstValue != secondValue:  # If values are not equal
            differenceCount += 1  # Increment the difference counter

    # Step 7: Determine if the two sets are considered similar
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 8: Execute the main function when the script runs
if __name__ == "__main__":
    main()
