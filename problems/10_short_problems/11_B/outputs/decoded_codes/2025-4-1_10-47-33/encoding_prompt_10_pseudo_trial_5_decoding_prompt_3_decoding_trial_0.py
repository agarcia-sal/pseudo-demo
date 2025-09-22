def main():
    # Assume n is an integer input from the user
    n = abs(int(input()))  # Read input and convert to absolute integer

    i = 0  # Initialize i to 0

    while True:
        s = (i * (i + 1)) // 2  # Calculate the sum of the first i integers
        m = s - n  # Calculate the difference between sum and n

        if s == n:  # Check if the sum equals n
            print(i)  # Output the value of i
            break  # Exit the loop
        
        elif s > n:  # Check if the sum exceeds n
            if m % 2 == 0:  # Check if the difference is even
                print(i)  # Output the value of i
                break  # Exit the loop
        
        i += 1  # Increment i by 1

# Call the main function to execute the code
main()
