# Initialize the value of n by taking the absolute value of the user input
n = abs(int(input()))
# Initialize the counter variable i to 0
i = 0

# Start an infinite loop to repeatedly check conditions
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2
    
    # Calculate the difference between the sum and n
    m = s - n
    
    # Check if the calculated sum is equal to n
    if s == n:
        print(i)  # Print the current value of i
        break  # Exit the loop

    # Check if the sum exceeds n
    if s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Print the current value of i
            break  # Exit the loop

    # Increment the counter variable i
    i += 1
