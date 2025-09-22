def main():
    # Read input for two sets of numbers
    first_input = input()  # Read the first set of numbers as a string
    second_input = input()  # Read the second set of numbers as a string

    # Split the input strings into lists of numbers
    first_list = first_input.split()  # Split first input string into a list
    second_list = second_input.split()  # Split second input string into a list

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the first three numbers in both lists
    for index in range(3):  # Loop over the first three indices
        # Convert the current elements to integers
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer

        # Check if the numbers are different
        if first_number != second_number:  # If numbers are not equal
            # Increment the differences counter
            difference_count += 1  # Increase difference count by 1

    # Determine output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Print "YES"
    else: 
        print("NO")  # Print "NO"

# Entry point for the program
if __name__ == "__main__":  # Check if this file is run as the main module
    main()  # Call the main function
