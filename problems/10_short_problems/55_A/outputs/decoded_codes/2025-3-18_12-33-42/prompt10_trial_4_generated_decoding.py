def main():
    # Read an integer input from user
    n = int(input())
    
    # Initialize a list 'b' with 'True' values of size 'n'
    b = [True] * n
    
    # Initialize control variables
    j = 0
    i = 1
    
    # Loop until 'i' exceeds 500,000
    while i <= 500000:
        # If the current index in 'b' is True, set it to False
        if b[j]:
            b[j] = False
        
        # Increment 'i' by 1
        i += 1
        
        # Update index 'j' using modulus to wrap around the list
        j = (j + i) % n
    
    # Create a list 'x' containing all True values from 'b'
    x = [value for value in b if value]
    
    # Check if 'x' is empty and print the appropriate result
    if len(x) == 0:
        print('YES')
    else:
        print('NO')


# Entry point of the program
if __name__ == "__main__":
    main()
