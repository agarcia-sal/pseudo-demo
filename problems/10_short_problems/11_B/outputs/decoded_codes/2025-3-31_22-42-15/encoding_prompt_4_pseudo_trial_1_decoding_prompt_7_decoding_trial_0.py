# Function to get the absolute value of user input and find the integer
def find_integer():
    # Get the absolute value of user input and convert it to an integer
    n = abs(int(input()))

    # Initialize variable to track the current number
    i = 0

    # Infinite loop to find the desired integer
    while True:
        # Calculate the sum of the first 'i' integers
        s = (i * (i + 1)) // 2  # Using integer division

        # Calculate the difference between the sum and 'n'
        m = s - n

        # Check if the sum equals 'n'
        if s == n:
            print(i)  # Output the current number
            break  # Exit the loop

        # Check if the sum exceeds 'n'
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the current number
                break  # Exit the loop

        # Increment 'i' for the next iteration
        i += 1  # Increase 'i' by 1

# Call the function to execute
find_integer()
