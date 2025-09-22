# Initialize Variables
n = abs(int(input()))  # Getting the absolute value of the input integer
i = 0  # Counter for current integer candidate

# Loop Indefinitely
while True:
    # Calculate Sum
    s = (i * (i + 1)) // 2  # Compute the sum of first i integers

    # Determine Difference
    m = s - n  # Calculate the difference

    # Check for Conditions
    if s == n:
        print(i)  # Print the value of i
        break  # Exit the loop

    if s > n:
        if m % 2 == 0:  # Check if the difference m is even
            print(i)  # Print the value of i
            break  # Exit the loop

    # Increment Counter
    i += 1  # Increase the value of i by 1 to check the next integer
