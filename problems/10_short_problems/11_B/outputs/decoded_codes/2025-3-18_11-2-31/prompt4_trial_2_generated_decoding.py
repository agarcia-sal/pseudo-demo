# Start by reading the absolute value of an integer input
n = abs(int(input()))

# Initialize a counter variable
i = 0

# Begin an indefinite loop
while True:
    # Calculate the sum of first 'i' natural numbers
    s = (i * (i + 1)) // 2  # Using integer division for clarity
    
    # Calculate the difference between the sum and the input number
    m = s - n

    # Check if the sum equals the input number
    if s == n:
        print(i)
        break  # Exit the loop if sum equals input number
    # Check if the sum exceeds the input number
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:  # Check the evenness of the difference
            print(i)
            break  # Exit the loop if difference is even

    # Increment the counter for the next iteration
    i += 1
