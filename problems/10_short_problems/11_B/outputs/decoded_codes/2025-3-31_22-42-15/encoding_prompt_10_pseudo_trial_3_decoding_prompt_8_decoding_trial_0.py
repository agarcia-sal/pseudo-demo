n = abs(int(input()))
i = 0

while True:
    s = (i * (i + 1)) // 2  # Calculate the sum of the first i natural numbers
    m = s - n                # Calculate the difference between s and n

    if s == n:
        print(i)             # Output the value of i if the sum equals n
        break                # Exit the loop
    
    elif s > n:
        if m % 2 == 0:       # Check if m is even
            print(i)         # Output the value of i if m is even
            break            # Exit the loop
    
    i += 1                   # Move to the next integer
