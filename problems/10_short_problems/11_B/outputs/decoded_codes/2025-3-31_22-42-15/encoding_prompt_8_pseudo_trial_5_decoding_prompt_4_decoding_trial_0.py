def find_non_negative_integer():
    # Start the process
    # Get Input
    desired_sum = abs(int(input()))  # Convert the input to an absolute integer

    # Initialize a counter
    i = 0  # This will track the number of terms

    # Loop indefinitely
    while True:
        # Calculate the sum of the first i natural numbers
        sum_of_first_i = (i * (i + 1)) // 2  # Using integer division to avoid float

        # Determine the difference from the desired sum
        difference = sum_of_first_i - desired_sum

        # Check conditions
        if sum_of_first_i == desired_sum:
            print(i)  # If they are equal, print the value of i
            break  # Exit the loop

        if sum_of_first_i > desired_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(i)  # Print i and exit
                break  # Exit the loop

        # Increment the counter
        i += 1  # Move to the next integer

# Call the function to execute the program
find_non_negative_integer()
