def main():
    # Step 1: Read two lines of input from the user
    firstLine = input()  # User inputs the first set of numbers as a string
    secondLine = input()  # User inputs the second set of numbers as a string

    # Step 2: Split the input lines into lists of strings
    firstList = firstLine.split()  # Splitting the first line into a list of strings
    secondList = secondLine.split()  # Splitting the second line into a list of strings

    # Step 3: Initialize a counter for differences
    differenceCount = 0  # Initialize a counter to track differences

    # Step 4: Loop through the first three elements of each list
    for index in range(3):  # Loop from index 0 to 2
        # Convert strings to integers
        firstNumber = int(firstList[index])  # Convert current item from first list to integer
        secondNumber = int(secondList[index])  # Convert current item from second list to integer
        
        # Step 5: Compare numbers and count differences
        if firstNumber != secondNumber:  # Check if the numbers are different
            differenceCount += 1  # Increment the difference count if they differ

    # Step 6: Check if the number of differences is less than three
    if differenceCount < 3:  # If the count of differences is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Call the main function to execute the program
main()
