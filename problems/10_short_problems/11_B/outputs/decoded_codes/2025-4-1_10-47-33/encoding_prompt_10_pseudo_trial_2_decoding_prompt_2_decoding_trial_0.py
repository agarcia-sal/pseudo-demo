# Assume n is a non-negative integer input by the user
n = abs(int(input()))  # Read input and set n to its absolute value

# Initialize variable i to count the iterations
i = 0

# Start an infinite loop to calculate triangular numbers
while True:
    # Calculate the i-th triangular number
    s = (i * (i + 1)) // 2  # Use integer division for correct result

    # Calculate the difference between the triangular number and n
    m = s - n

    # Check if the triangular number is equal to n
    if s == n:
        print(i)  # Output the value of i
        break  # Exit the loop

    # Check if the triangular number exceeds n
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Output the value of i
            break  # Exit the loop

    # Increment i for the next iteration
    i += 1
