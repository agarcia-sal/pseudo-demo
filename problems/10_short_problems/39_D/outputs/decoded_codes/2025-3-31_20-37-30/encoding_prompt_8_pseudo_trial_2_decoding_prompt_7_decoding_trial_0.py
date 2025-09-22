def main():
    # Step 1: Get two strings of numbers from the user
    inputString1 = input()  # User input for the first set of numbers
    inputString2 = input()  # User input for the second set of numbers

    # Step 2: Split the input strings into individual numbers
    numbersList1 = inputString1.split()  # Split first string into list of numbers
    numbersList2 = inputString2.split()  # Split second string into list of numbers

    # Step 3: Initialize a counter for differences
    differenceCount = 0  # Counter to keep track of differences

    # Step 4: Compare each corresponding number in the two lists
    for index in range(3):  # Loop through the first three indices
        number1 = int(numbersList1[index])  # Convert string to integer for the first number
        number2 = int(numbersList2[index])  # Convert string to integer for the second number

        # Step 5: Check if the numbers are different
        if number1 != number2:  # Compare the two numbers
            differenceCount += 1  # If they differ, increment the counter

    # Step 6: Determine if the count of differences is less than 3
    if differenceCount < 3:  # Check if differences are fewer than 3
        print("YES")  # Print YES if the differences are fewer than 3
    else:
        print("NO")  # Otherwise, print NO

# Trigger the main function if the script is run directly
if __name__ == "__main__":
    main()
