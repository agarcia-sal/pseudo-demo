def main():
    # Gather input from the user
    input1 = input()  # Read first set of numbers
    input2 = input()  # Read second set of numbers

    # Split the input strings into lists of numbers
    firstList = input1.split()  # Split first input into a list
    secondList = input2.split()  # Split second input into a list

    # Initialize a variable to count differences
    differenceCount = 0

    # Loop through each index of the lists (assuming both lists have exactly 3 elements)
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current elements of both lists to integers
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Check if the values at this index are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1

    # After comparing all positions, decide on the output
    if differenceCount < 3:
        print("YES")  # Output YES if fewer than 3 differences
    else:
        print("NO")   # Output NO if 3 or more differences

# Execute the main function
if __name__ == "__main__":
    main()
