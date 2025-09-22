def find_matching_counter():
    # Step 1: Read the absolute integer input from the user
    input_value = abs(int(input()))

    # Step 2: Initialize a counter variable
    counter = 0

    # Step 3: Create an indefinite loop to calculate the required values
    while True:
        # Step 4: Calculate the sum of numbers from 0 to the current counter
        current_sum = (counter * (counter + 1)) // 2  # Using integer division

        # Step 5: Calculate the difference between the current sum and the input value
        difference = current_sum - input_value

        # Step 6: Check if current sum equals the input value
        if current_sum == input_value:
            # Step 6a: Print the current counter and exit the loop
            print(counter)
            break  # Using 'break' to exit the loop

        # Step 7: Check if current sum exceeds the input value
        elif current_sum > input_value:
            # Step 7a: Check if the difference is an even number
            if difference % 2 == 0:
                # Step 7b: Print the current counter and exit the loop
                print(counter)
                break  # Using 'break' to exit the loop

        # Step 8: Increment the counter for the next iteration
        counter += 1

# Call the function to execute
find_matching_counter()
