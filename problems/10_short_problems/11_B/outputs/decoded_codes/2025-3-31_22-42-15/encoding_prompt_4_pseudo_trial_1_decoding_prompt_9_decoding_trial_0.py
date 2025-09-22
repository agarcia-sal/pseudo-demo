# Function to get the absolute value of a number
def absolute_value(num):
    return abs(num)

# Main execution starts here
n = absolute_value(int(input()))  # Get the absolute value of user input and convert it to an integer
i = 0  # Initialize variable to track the current number

while True:  # Infinite loop to find the desired integer
    s = (i * (i + 1)) // 2  # Calculate the sum of the first 'i' integers
    m = s - n  # Calculate the difference between the sum and 'n'

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
    i += 1
