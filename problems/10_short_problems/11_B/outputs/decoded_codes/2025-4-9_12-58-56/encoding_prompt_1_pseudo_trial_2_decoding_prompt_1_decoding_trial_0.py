# Step 1: Receive Input
inputNumber = abs(int(input()))  # Get a number from the user and store it as an absolute integer.

# Step 2: Initialize Counter
counter = 0  # Create a counter variable and set it to 0.

# Step 3: Start an Infinite Loop
while True:  # Repeat indefinitely until a condition is met to exit the loop.

    # Step 3.1: Calculate Triangular Number
    triangularNumber = counter * (counter + 1) / 2  # Calculate the triangular number.

    # Step 3.2: Calculate Difference
    difference = triangularNumber - inputNumber  # Compute the difference.

    # Step 3.3: Check for Exact Match
    if triangularNumber == inputNumber:  # If there's an exact match:
        print(counter)  # Print the counter.
        break  # Exit the loop.

    # Step 3.4: Check for Exceeding Input
    elif triangularNumber > inputNumber:  # If the triangular number exceeds the input:
        if difference % 2 == 0:  # Check if the difference is even:
            print(counter)  # Print the counter.
            break  # Exit the loop.

    # Step 3.5: Increment Counter
    counter += 1  # Increment the counter for the next iteration.
