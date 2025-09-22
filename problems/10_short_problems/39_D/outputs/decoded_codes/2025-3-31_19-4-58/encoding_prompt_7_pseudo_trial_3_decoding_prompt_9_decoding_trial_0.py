def doMain():
    # Read two lines of input from the user
    text1 = input()
    text2 = input()

    # Split the input lines into lists of strings
    list1 = text1.split()
    list2 = text2.split()
    
    # Initialize a variable to count differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements from strings to integers
        number1 = int(list1[index])
        number2 = int(list2[index])
        
        # Compare the two numbers
        if number1 != number2:
            # Increment differenceCount by 1 
            differenceCount += 1 
    
    # Check if the count of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
if __name__ == "__main__":
    doMain()
