def doMain():
    # Read two lines of input from the user
    text1 = input()
    text2 = input()

    # Split the input lines into lists of strings
    list1 = text1.split()  # Split the first input
    list2 = text2.split()  # Split the second input

    # Initialize a variable to count differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):  # Iterating over the first three indices
        # Convert the elements from strings to integers
        number1 = int(list1[index])  # Convert the first number
        number2 = int(list2[index])  # Convert the second number

        # Compare the two numbers
        if number1 != number2:  # Check if they are different
            differenceCount += 1  # Increment difference count

    # Check if the count of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Output YES if fewer than three differences
    else:
        print("NO")   # Output NO otherwise

# Start the program by calling the main function
if __name__ == "__main__":
    doMain()  # Call the main function to execute
