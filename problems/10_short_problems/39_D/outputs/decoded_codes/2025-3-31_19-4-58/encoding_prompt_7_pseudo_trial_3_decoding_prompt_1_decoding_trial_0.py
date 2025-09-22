def doMain():
    # Read two lines of input from the user
    text1 = input()  # User input for the first set of numbers
    text2 = input()  # User input for the second set of numbers

    # Split the input lines into lists of strings
    list1 = text1.split()  # Split the first line into a list
    list2 = text2.split()  # Split the second line into a list
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the elements from strings to integers
        number1 = int(list1[index])  # Convert list1 element to integer
        number2 = int(list2[index])  # Convert list2 element to integer
        
        # Compare the two numbers
        if number1 != number2:  # Check if they are different
            differenceCount += 1  # Increment the difference count
    
    # Check if the count of differences is less than 3
    if differenceCount < 3:  # If differences are fewer than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Otherwise, print NO

# Start the program by calling the main function
if __name__ == "__main__":  # Check if the script is executed as the main program
    doMain()  # Call the main function
