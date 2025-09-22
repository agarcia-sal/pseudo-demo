def main_procedure():
    # Read two lines of input from the user
    user_input_1 = input()  # First set of numbers
    user_input_2 = input()  # Second set of numbers

    # Split the input strings into lists of individual string numbers
    number_list_1 = user_input_1.split()  # Split first input
    number_list_2 = user_input_2.split()  # Split second input

    difference_count = 0  # Initialize a counter for differences

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert input number strings to integers
        number_a = int(number_list_1[index])  # Convert first input number to integer
        number_b = int(number_list_2[index])  # Convert second input number to integer

        # Check if the two numbers are different
        if number_a != number_b:
            difference_count += 1  # Increment the difference counter

    # Determine if the count of differences is less than 3
    if difference_count < 3:
        print("YES")  # Output "YES" if fewer than 3 differences
    else:
        print("NO")   # Output "NO" if 3 or more differences

# Execute the main procedure when the program starts
if __name__ == "__main__":
    main_procedure()
