def main_procedure():
    # Get the first set of numbers from the user
    first_number_set = input()  # e.g., "5 10 15"

    # Get the second set of numbers from the user
    second_number_set = input()  # e.g., "5 20 15"

    # Split the input strings into lists of numbers
    first_number_list = first_number_set.split()  # ["5", "10", "15"]
    second_number_list = second_number_set.split()  # ["5", "20", "15"]

    # Initialize a counter for the number of differing values
    difference_count = 0

    # Loop through indices from 0 to 2 (for the three number pairs)
    for index in range(3):  # Looping through indices 0, 1, 2
        # Convert the current values from strings to integers
        first_value = int(first_number_list[index])  # Convert to integer
        second_value = int(second_number_list[index])  # Convert to integer

        # Check if the values are different
        if first_value != second_value:  # If values are not equal
            # Increase the count of differences
            difference_count += 1  # Increment difference counter

    # Determine if the number of differences is less than 3
    if difference_count < 3:  # If differences are less than 3
        # Print "YES" if they are similar enough
        print("YES")
    else:
        # Print "NO" if they differ significantly
        print("NO")

# Start the program by calling the main_procedure
main_procedure()
