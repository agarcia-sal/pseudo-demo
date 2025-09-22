# Define a function to get the absolute value of user input and convert it to an integer
n = abs(int(input()))  # Get the user input and convert it to an absolute integer

# Initialize variable to track the current number
i = 0

# Infinite loop to find the desired integer
while True:
    # Calculate the sum of the first 'i' integers
    sum_of_integers = (i * (i + 1)) / 2

    # Calculate the difference between the sum and 'n'
    difference = sum_of_integers - n

    # Check if the sum equals 'n'
    if sum_of_integers == n:
        print(i)  # Output the current number
        break  # Exit the loop

    # Check if the sum exceeds 'n'
    elif sum_of_integers > n:
        # Check if the difference is even
        if difference % 2 == 0:
            print(i)  # Output the current number
            break  # Exit the loop

    # Increment 'i' for the next iteration
    i += 1  # Increment i
