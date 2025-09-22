def main():
    # Read input value for n
    n = int(input())

    # Initialize a list of boolean values, all set to True
    b = [True] * n

    j = 0
    i = 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current position in the list is True
        if b[j]:
            # Mark the position as False
            b[j] = False
        
        # Increment i
        i += 1
        
        # Update the index j in a circular manner
        j = (j + i) % n

    # Create a list x of True values from b
    x = [value for value in b if value]

    # Check if there are any True values remaining
    if len(x) == 0:
        print('YES')
    else:
        print('NO')

# Run the main function
main()
