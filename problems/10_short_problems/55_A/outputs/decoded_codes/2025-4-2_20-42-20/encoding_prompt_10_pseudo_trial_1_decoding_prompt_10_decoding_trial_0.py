def main():
    # Read input value for n
    n = int(input())
    
    # Create a list b of size n, initializing all elements to True
    b = [True] * n
    
    # Initialize j and i
    j = 0
    i = 1

    # Main loop that runs until i exceeds 500,000
    while i <= 500000:
        # Check if the current index j in list b is True
        if b[j]:
            # Set the current index to False
            b[j] = False
            
        # Increment i by 1
        i += 1
        
        # Update j using modular arithmetic
        j = (j + i) % n

    # Create a new list x that contains all True values in b
    x = [value for value in b if value]
    
    # Check if the list x is empty
    if len(x) == 0:
        print('YES')  # Print YES if x is empty
    else:
        print('NO')   # Print NO if x is not empty

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
