def main():
    # Step 1: Read input from the user
    userInput1 = input()
    userInput2 = input()

    # Step 2: Split the inputs into lists of strings
    inputList1 = userInput1.split()
    inputList2 = userInput2.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare the elements of the two lists
    for index in range(3):
        # Convert string elements to integers for comparison
        number1 = int(inputList1[index])
        number2 = int(inputList2[index])

        # Step 5: Check if the numbers are different
        if number1 != number2:
            # Increment the difference counter
            differenceCount += 1

    # Step 6: Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the Main function when the program is run
if __name__ == "__main__":
    main()
