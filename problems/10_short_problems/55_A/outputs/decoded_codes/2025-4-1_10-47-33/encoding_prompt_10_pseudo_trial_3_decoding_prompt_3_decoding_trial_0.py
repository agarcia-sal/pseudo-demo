def main():
    # Step 1: Input the size of the array
    n = int(input())  # Read the input value for the size of the array
    
    # Step 2: Initialize a list of Boolean values, all set to True
    b = [True] * n
    
    # Step 3: Initialize variables for looping
    j = 0  # Current index in the list
    i = 1  # Incrementing value
    
    # Step 4: Loop to process values while i is less than or equal to 500000
    while i <= 500000:
        if b[j]:  # Check if the current position j in the list b is True
            b[j] = False  # Mark position j as False
            
        i += 1  # Move to the next value
        j = (j + i) % n  # Update position j using modulo operation to wrap around
    
    # Step 5: Create a new list x containing only True values from b
    x = [value for value in b if value]  # List comprehension to filter True values
    
    # Step 6: Check if the list x is empty and print the result
    if not x:  # If x is empty
        print("YES")  # No True values left in b
    else:
        print("NO")   # There are still True values in b

# Call the main function to execute the program
if __name__ == "__main__":
    main()
