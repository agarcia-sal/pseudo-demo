# Define the main function to execute the logic
def main():
    # Input: Read an integer value 'n' from user
    n = int(input())

    # Initialize a boolean list 'b' of size 'n' with all values set to True
    b = [True] * n

    # Initialize variables 
    j = 0  # Index for the list 'b'
    i = 1  # Counter that will increment in the loop

    # Loop to perform operations while 'i' is less than or equal to 500000
    while i <= 500000:
        # Check if the current index 'j' in the list 'b' is True
        if b[j]:
            # Set the current index 'j' to False
            b[j] = False
        
        # Increment 'i' by 1
        i += 1
        
        # Update index 'j' by adding the current value of 'i', and taking modulo n
        j = (j + i) % n

    # Filter the list 'b' to collect all elements that are still True
    x = [val for val in b if val]

    # Check if the filtered list 'x' is empty
    if len(x) == 0:
        # Output 'YES' if list 'x' is empty
        print('YES')
    else:
        # Output 'NO' if list 'x' is not empty
        print('NO')

# Entry point of the script
if __name__ == "__main__":
    main()
