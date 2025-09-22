def main():
    # Step 1: Get absolute value of user input
    n = abs(int(input()))
    
    # Step 2: Initialize i
    i = 0
    
    # Step 3: Repeat indefinitely
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division
        
        # Calculate the difference between s and n
        m = s - n
        
        # Check if s is equal to n
        if s == n:
            print(i)  # Print the value of i
            break  # Exit the loop
        
        # Check if s is greater than n
        elif s > n:
            # Check if m is even
            if m % 2 == 0:
                print(i)  # Print the value of i
                break  # Exit the loop
        
        # Increment i for the next iteration
        i += 1

# Invoke the main function
if __name__ == "__main__":
    main()
