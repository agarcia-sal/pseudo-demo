def find_result_based_on_input():
    # Step 1: Get the absolute value of the user input
    integer_input = int(input())
    input_value = abs(integer_input)

    # Initialize a counter variable
    counter = 0

    # Step 2: Continuous loop until a condition is met
    while True:
        # Calculate the sum of the first 'counter' integers
        sum_of_integers = (counter * (counter + 1)) // 2

        # Calculate the difference between the current sum and the input value
        difference = sum_of_integers - input_value

        # Step 3: Check if the current sum equals the input value
        if sum_of_integers == input_value:
            print(counter)  # Output the current counter
            break  # Exit the loop

        # Step 4: Check if the current sum exceeds the input value
        elif sum_of_integers > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Output the current counter
                break  # Exit the loop

        # Step 5: Increment the counter for the next iteration
        counter += 1

# Call the function to execute the code
find_result_based_on_input()
