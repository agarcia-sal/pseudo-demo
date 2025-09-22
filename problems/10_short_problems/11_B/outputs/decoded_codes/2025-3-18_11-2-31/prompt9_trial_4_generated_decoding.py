# Receive Input
input_number = int(input())  # Read an integer from the user
n = abs(input_number)  # Set n to the absolute value of input_number

# Initialize Variables
i = 0  # Start i at 0

# Start Infinite Loop
while True:
    # Calculate sum of the first i integers
    sum_of_first_i = (i * (i + 1)) // 2  # Use integer division to ensure the result is an integer
    difference = sum_of_first_i - n  # Calculate the difference

    # Check for a Match
    if sum_of_first_i == n:
        print(i)  # Print the value of i
        break  # Exit the loop

    # Check for Greater Sum
    if sum_of_first_i > n:
        if difference % 2 == 0:  # Check if the difference is an even number
            print(i)  # Print the value of i
            break  # Exit the loop

    # Increment Counter
    i += 1  # Increase the value of i by 1
