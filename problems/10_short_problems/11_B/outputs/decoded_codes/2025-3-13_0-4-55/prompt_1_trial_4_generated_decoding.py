# Initialize Variables
n = abs(int(input()))  # Read the integer and take its absolute value
i = 0  # Counter for current integer candidate

# Loop Indefinitely
while True:
    # Calculate Sum
    s = (i * (i + 1)) / 2  # Sum of the first i integers

    # Determine Difference
    m = s - n  # Difference between sum and n

    # Check for Conditions
    if s == n:
        print(i)  # Print the current integer and exit
        break  # Exit the loop
    
    if s > n:
        if m % 2 == 0:  # Check if the difference is even
            print(i)  # Print the current integer and exit
            break  # Exit the loop

    # Increment Counter
    i += 1  # Move to the next integer
