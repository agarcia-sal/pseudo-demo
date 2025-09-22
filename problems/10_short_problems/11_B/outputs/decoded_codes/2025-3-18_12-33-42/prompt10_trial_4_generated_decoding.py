def main():
    # Get the absolute value of the user input
    n = abs(int(input()))
    
    # Initialize the loop counter
    i = 0
    
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        # Calculate the difference between s and n
        m = s - n

        if s == n:
            print(i)  # Output i if s matches n
            break  # Exit loop
        elif s > n:
            if m % 2 == 0:  # Check if m is even
                print(i)  # Output i if m is even
                break  # Exit loop
        
        # Increment i by 1 for the next iteration
        i += 1

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
