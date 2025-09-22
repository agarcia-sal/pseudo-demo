def main():
    # Gather input from the user
    input1 = input()
    input2 = input()
    
    # Split the input strings into lists of numbers
    firstList = input1.split()
    secondList = input2.split()
    
    # Initialize a variable to count differences
    differenceCount = 0

    # Loop through each index of the lists (assuming both lists have exactly 3 elements)
    for index in range(3):
        # Convert the current elements of both lists to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values at this index are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1

    # After comparing all positions, decide on the output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
