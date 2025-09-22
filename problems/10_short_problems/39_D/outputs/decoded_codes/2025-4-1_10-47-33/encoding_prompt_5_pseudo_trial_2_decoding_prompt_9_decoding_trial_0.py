def main():
    # Step 1: Accept user input for two lines of numbers
    t1 = input()  # First line of input
    t2 = input()  # Second line of input

    # Step 2: Split the input lines into lists of strings
    tt1 = t1.split()  # Convert t1 into a list of strings
    tt2 = t2.split()  # Convert t2 into a list of strings

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each pair of numbers
    for index in range(3):  # Loop for three pairs
        # Step 4a: Convert the strings to integers for comparison
        number1 = int(tt1[index])  # Convert to integer
        number2 = int(tt2[index])  # Convert to integer

        # Step 4b: Check if the two numbers differ
        if number1 != number2:  # If they are not equal
            difference_count += 1  # Increment the difference count

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:  # Check if differences are less than 3
        print("YES")  # The pairs differ in less than three positions
    else:
        print("NO")  # The pairs differ in three or more positions

# Execute the main function when the program starts
main()
