def do_main():
    # Step 1: Read two lines of input and store them in variables
    first_input = input()  # Read first input string
    second_input = input()  # Read second input string

    # Step 2: Split the input strings into lists of substrings
    list_first_input = first_input.split()  # Split t1 into a list
    list_second_input = second_input.split()  # Split t2 into a list

    # Step 3: Initialize a variable to count differences
    difference_count = 0  # Initialize difference count to 0

    # Step 4: Compare elements of the two lists
    for index in range(3):  # Loop over indices 0 to 2
        # Convert the substring to an integer for comparison
        first_number = int(list_first_input[index])  # Set a to integer value of tt1[index]
        second_number = int(list_second_input[index])  # Set b to integer value of tt2[index]

        # Step 5: Increment the count if the numbers are not equal
        if first_number != second_number:  # If a is not equal to b
            difference_count += 1  # Increment difference count by 1

    # Step 6: Determine output based on the number of differences
    if difference_count < 3:  # If difference count is less than 3
        print("YES")  # Print "YES"
    else:  # Else
        print("NO")  # Print "NO"

# Step 7: Main execution block
if __name__ == "__main__":  # If the script is executed as the main program
    do_main()  # Call do_main function
