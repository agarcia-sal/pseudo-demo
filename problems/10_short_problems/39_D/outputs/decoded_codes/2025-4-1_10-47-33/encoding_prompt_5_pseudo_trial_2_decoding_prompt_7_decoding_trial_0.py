def main():
    # Step 1: Accept user input for two lines of numbers
    t1 = input()  # First line of numbers
    t2 = input()  # Second line of numbers

    # Step 2: Split the input lines into lists of strings
    tt1 = t1.split()  # Convert the first line into a list of strings
    tt2 = t2.split()  # Convert the second line into a list of strings

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare each pair of numbers
    for index in range(3):  # Loop through indices 0 to 2
        # Step 4a: Convert the strings to integers for comparison
        number1 = int(tt1[index])  # Convert the first number to an integer
        number2 = int(tt2[index])  # Convert the second number to an integer

        # Step 4b: Check if the two numbers differ
        if number1 != number2:  # If the numbers are not equal
            differenceCount += 1  # Increment the difference counter

    # Step 5: Determine the output based on the number of differences
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the main function when the program starts
main()
