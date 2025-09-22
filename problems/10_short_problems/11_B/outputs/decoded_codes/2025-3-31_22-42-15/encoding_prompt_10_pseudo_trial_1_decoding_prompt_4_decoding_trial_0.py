def main():
    # Step 2: Declare Variables
    n = abs(int(input()))  # Get the absolute value of the integer input
    i = 0  # Initialize the counter
    
    while True:  # Step 3: Begin Infinite Loop
        # Compute the triangular number s
        s = (i * (i + 1)) // 2  # Using integer division for accuracy
        
        # Calculate m as the difference between s and n
        m = s - n 
        
        # Step 4: Check Conditions
        if s == n:
            print(i)  # Display the value of i
            break  # Exit the loop
        elif s > n:
            if m % 2 == 0:  # Check if m is an even number
                print(i)  # Display the value of i
                break  # Exit the loop
        
        i += 1  # Step 5: Increment i by 1

# Execute the main function
if __name__ == "__main__":
    main()
