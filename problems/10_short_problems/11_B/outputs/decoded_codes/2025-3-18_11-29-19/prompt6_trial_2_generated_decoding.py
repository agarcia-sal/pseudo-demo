# Read an integer value from user input and convert it to absolute value
n = abs(int(input()))

# Initialize variable 'i' to 0
i = 0

# Repeat forever (infinite loop)
while True:
    # Calculate the sum 's' as the sum of the first 'i' natural numbers
    s = (i * (i + 1)) // 2  # Using integer division

    # Calculate the difference 'm' between 's' and 'n'
    m = s - n

    # If 's' is equal to 'n'
    if s == n:
        print(i)  # Print the value of 'i'
        break  # Exit the loop

    # If 's' is greater than 'n'
    if s > n:
        # If 'm' is an even number
        if m % 2 == 0:
            print(i)  # Print the value of 'i'
            break  # Exit the loop

    # Increment 'i' by 1
    i += 1
