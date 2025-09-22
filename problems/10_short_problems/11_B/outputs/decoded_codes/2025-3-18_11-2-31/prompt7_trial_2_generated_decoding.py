def find_integer_based_on_input():
    # Prompt the user for an integer input and assign its absolute value to userInput
    user_input = int(input())
    user_input = abs(user_input)  # Ensure the absolute value is used
    index = 0  # Initialize index to 0

    # Loop indefinitely until a condition is met to break it
    while True:
        # Calculate the sum of the first index integers using the formula
        sum_value = (index * (index + 1)) // 2  # Using integer division

        # Calculate the difference between sum_value and userInput
        difference_value = sum_value - user_input

        # Check if sum_value equals userInput
        if sum_value == user_input:
            print(index)  # Output the index
            break  # Break the loop if an exact match is found
        # If sum_value is greater than userInput
        elif sum_value > user_input:
            # Check if the difference is even
            if difference_value % 2 == 0:
                print(index)  # Output the index
                break  # Break the loop if the difference is even

        # Increment index by 1 to check the next number
        index += 1

# Invoke the function
find_integer_based_on_input()
