def main():
    # Read two lines of input from the user
    input_line_1 = input()
    input_line_2 = input()

    # Split the input into lists of strings
    list1 = input_line_1.split()
    list2 = input_line_2.split()

    # Initialize a counter for differing elements
    differing_count = 0

    # Compare the elements of the two lists up to the third element
    for index in range(3):  # Loop through the first three elements
        # Convert the string elements to integers
        value1 = int(list1[index])
        value2 = int(list2[index])

        # If the values differ, increment the differing count
        if value1 != value2:
            differing_count += 1

    # Determine if the number of differences is less than 3
    if differing_count < 3:
        print("YES")  # Output result indicating fewer than 3 differences
    else:
        print("NO")   # Output result indicating 3 or more differences

# Execute the main function if the script is run as the main program
if __name__ == "__main__":
    main()
