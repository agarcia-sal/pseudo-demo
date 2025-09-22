def find_counter_for_user_input():
    # Read input from the user
    user_input = abs(int(input()))

    # Initialize a counter
    counter = 0

    # Loop indefinitely until a condition is met
    while True:
        # Calculate the sum of numbers from 0 to counter
        sum_value = (counter * (counter + 1)) // 2

        # Calculate the difference between sum and user input
        difference = sum_value - user_input

        # Check if the sum equals the user input
        if sum_value == user_input:
            # Print the counter if they are equal and break the loop
            print(counter)
            break

        # Check if the sum exceeds the user input
        elif sum_value > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the counter if difference is even and break the loop
                print(counter)
                break

        # Increment the counter for the next iteration
        counter += 1

# Call the function to execute
find_counter_for_user_input()
