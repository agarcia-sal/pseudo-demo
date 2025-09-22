def main():
    # Prompt the user for input
    first_input = input()  # Get first set of numbers
    second_input = input()  # Get second set of numbers

    # Split the inputs into lists of numbers
    first_numbers = first_input.split()  # Split by spaces
    second_numbers = second_input.split()  # Split by spaces

    # Initialize a variable to count differences
    difference_count = 0

    # Compare the numbers at each position
    for index in range(3):  # Loop through indices 0 to 2
        first_number = int(first_numbers[index])  # Convert string to integer
        second_number = int(second_numbers[index])  # Convert string to integer
        
        # If the numbers differ, increment the difference count
        if first_number != second_number:  # Check for inequality
            difference_count += 1  # Increment the count

    # Determine the result based on the number of differences
    if difference_count < 3:  # Check if differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Start the program
main()
