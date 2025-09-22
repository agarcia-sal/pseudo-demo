# The following program implements the described pseudocode

def main():
    # Step 1: Input the number n
    n = int(input())
    
    # Step 2: Initialize a list b with TRUE values
    b = [True] * n  # Create a list of TRUE values of size n
    
    # Step 3: Initialize loop control variables
    j = 0
    i = 1
    
    # Step 4: Main loop to update the list b
    while i <= 500000:
        # Step 5: Check if current position j is marked TRUE
        if b[j]:  # If b[j] is TRUE
            b[j] = False  # Mark it as FALSE
        
        # Step 6: Increment i and update j for the next iteration
        i += 1  # Increment i by 1
        j = (j + i) % n  # Update j using modulo n to wrap around the list
    
    # Step 7: Create a list x with all TRUE values from list b
    x = [value for value in b if value]  # Filter TRUE values from b
    
    # Step 8: Check if list x is empty
    if len(x) == 0:
        print('YES')  # Print 'YES' if x is empty
    else:
        print('NO')  # Print 'NO' if x is not empty

# Call the main function
main()
