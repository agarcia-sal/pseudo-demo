# Get user input and convert it to an absolute integer
user_input = int(input())
n = abs(user_input)

# Initialize counter variable
i = 0

# Begin an infinite loop
while True:
    # Calculate the sum of the first 'i' integers
    sum_of_integers = (i * (i + 1)) / 2
    # Calculate the difference between the sum and input
    difference = sum_of_integers - n
    
    # Check if the calculated sum equals 'n'
    if sum_of_integers == n:
        print(i)  # Output the value of 'i'
        break  # Exit the loop

    # Check if the calculated sum is greater than 'n'
    elif sum_of_integers > n:
        # Check if the difference is even
        if difference % 2 == 0:
            print(i)  # Output the value of 'i'
            break  # Exit the loop

    # Increment 'i' for the next iteration
    i += 1
