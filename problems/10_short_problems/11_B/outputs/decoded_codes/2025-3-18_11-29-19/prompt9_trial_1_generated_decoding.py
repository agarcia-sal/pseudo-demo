# Receive Input
user_input = int(input())  # Get a number from the user and convert it to a non-negative integer

# Initialize Variables
i = 0

# Start an Infinite Loop
while True:
    # Calculate the Sum
    current_sum = i * (i + 1) // 2  # Use integer division

    # Determine the Difference
    difference = current_sum - user_input

    # Check for Exact Match
    if current_sum == user_input:
        print(i)
        break  # Exit the loop

    # Check for Exceeding Sum
    if current_sum > user_input:
        if difference % 2 == 0:  # Check if the difference is an even number
            print(i)
            break  # Exit the loop

    # Increment the Counter
    i += 1
