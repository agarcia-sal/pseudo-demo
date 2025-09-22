def doMain():
    # Prompt for user input
    inputString1 = input()
    inputString2 = input()

    # Process the input by splitting the strings into lists
    listOfValues1 = inputString1.split()
    listOfValues2 = inputString2.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Compare values in the two lists
    for index in range(3):  # Iterate over the first three indices
        valueA = int(listOfValues1[index])  # Convert to integer
        valueB = int(listOfValues2[index])  # Convert to integer
        
        if valueA != valueB:  # Check for differences
            differenceCount += 1  # Increment the counter if different

    # Output the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program if this script is run as a standalone program
if __name__ == "__main__":
    doMain()
