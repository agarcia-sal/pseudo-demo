# Start of program

# Step 1: Get the absolute value of user input as an integer
user_input = input()  # Take user input
n = abs(int(user_input))  # Convert input to integer and get the absolute value

# Step 2: Initialize a counter for the sum calculation
i = 0

# Step 3: Repeat indefinitely until a condition is met
while True:
    # Step 4: Calculate the sum of the first 'i' integers
    s = (i * (i + 1)) // 2

    # Step 5: Calculate the difference between the sum and user input
    m = s - n

    # Step 6: Check if the sum equals the user input
    if s == n:
        print(i)  # Step 6a: Print the current integer 'i' if the condition is met
        break  # Exit the loop

    # Step 7: Check if the sum is greater than the user input
    elif s > n:
        # Step 7a: Check if the difference is even
        if m % 2 == 0:
            print(i)  # Step 7b: Print the current integer 'i' if the condition is met
            break  # Exit the loop

    # Step 8: Increment 'i' for the next iteration
    i += 1  # Increase 'i' by 1 for the next calculation

# End of program
