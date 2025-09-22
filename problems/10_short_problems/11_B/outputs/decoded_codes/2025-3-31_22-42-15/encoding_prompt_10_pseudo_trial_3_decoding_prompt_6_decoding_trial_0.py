# Start the program
# Import the necessary function for absolute value
n = abs(int(input()))  # Read an integer input and convert it to its absolute value
i = 0  # Initialize a counter variable

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Use integer division since s will be an integer
    m = s - n  # Calculate the difference between s and n

    # Check if the sum equals n
    if s == n:
        print(i)  # Print the current value of i
        break  # Exit the loop

    # Check if the sum is greater than n
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Print the current value of i
            break  # Exit the loop

    i += 1  # Increment i to test the next integer
