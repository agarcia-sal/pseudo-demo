def main():
    # Step 1: Get input values
    firstInput = input()  # Read the first input string
    secondInput = input()  # Read the second input string

    # Step 2: Split the input strings into lists of strings
    firstList = firstInput.split()  # Split the first input by spaces
    secondList = secondInput.split()  # Split the second input by spaces

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare the corresponding elements of the two lists
    for index in range(3):  # We are only interested in the first three elements
        firstElement = int(firstList[index])  # Convert first list element to integer
        secondElement = int(secondList[index])  # Convert second list element to integer
        
        # If elements are different, increment the counter
        if firstElement != secondElement:
            differenceCount += 1  # Increment the difference count if they are not equal

    # Step 5: Determine the output based on the number of differences
    if differenceCount < 3:  # Check if differences are less than 3
        print("YES")  # Output "YES" if true
    else:
        print("NO")  # Otherwise, output "NO"

# Step 6: Execute the main function if the program is run as main
if __name__ == "__main__":
    main()  # Call the main function to execute the program
