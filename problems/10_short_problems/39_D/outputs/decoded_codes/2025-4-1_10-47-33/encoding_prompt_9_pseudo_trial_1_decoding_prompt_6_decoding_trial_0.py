def main():
    # Get two lines of input from the user
    first_input = input()  # First line of input
    second_input = input()  # Second line of input

    # Split the input strings into lists of numbers
    first_numbers = first_input.split()  # Split first input into a list of strings
    second_numbers = second_input.split()  # Split second input into a list of strings

    # Initialize a variable to count differences
    difference_count = 0 

    # Loop through the first three numbers in both lists
    for index in range(3):  # Loop over the indices of the first three elements
        # Convert the string numbers to integers
        first_number = int(first_numbers[index])  # Convert to integer
        second_number = int(second_numbers[index])  # Convert to integer
        
        # Check if the numbers at the same index are different
        if first_number != second_number:  # Compare the numbers
            difference_count += 1  # Increment the difference counter

    # Check if the number of differences is less than 3
    if difference_count < 3:  # Compare the difference count
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")  # Output if differences are 3 or more

# Start the program
main()  # Call the main function to execute
