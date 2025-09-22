# Start of the program

# Step 1: Get the absolute integer input
n = abs(int(input()))  # Read user input and convert it to its absolute value

# Step 2: Initialize the counter variable
i = 0  # Start the counter from 0

# Step 3: Begin an infinite loop to find the result
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Use integer division to get the sum

    # Calculate the difference between sum and input
    m = s - n  # Determine the difference

    # Step 4: Check if the sum equals n
    if s == n:
        print(i)  # Output i if the sum matches n
        break  # Exit the loop

    # Step 5: Check if the sum exceeds n
    elif s > n:
        # Step 6: Check if the difference is even
        if m % 2 == 0:
            print(i)  # Output i if the difference is even
            break  # Exit the loop

    # Increment the counter for the next iteration
    i += 1  # Move to the next natural number

# End of the program
