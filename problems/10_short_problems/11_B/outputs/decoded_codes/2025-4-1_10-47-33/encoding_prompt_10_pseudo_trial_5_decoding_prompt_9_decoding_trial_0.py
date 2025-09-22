# Begin execution of the program
n = abs(int(input()))  # Read and store absolute value of the integer input from user
i = 0  # Initialize variable i to 0

while True:  # Start an infinite loop
    s = (i * (i + 1)) // 2  # Calculate the sum of the first i integers
    m = s - n  # Calculate the difference between the sum and n

    if s == n:  # Check if the sum equals n
        print(i)  # Output the value of i
        break  # Exit the loop
    
    elif s > n:  # Check if the sum exceeds n
        if m % 2 == 0:  # Check if the difference is even
            print(i)  # Output the value of i
            break  # Exit the loop
    
    i += 1  # Increment i by 1
