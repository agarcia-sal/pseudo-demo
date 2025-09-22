def main():
    # Step 1: Read an integer input 'n'
    n = int(input())
    
    # Step 2: Create a list 'b' with 'n' elements, all set to True
    b = [True] * n
    
    # Step 3: Initialize index variables
    j = 0
    i = 1
    
    # Step 4: Loop while 'i' is less than or equal to 500,000
    while i <= 500000:
        # If the current element in 'b' at index 'j' is True
        if b[j]:
            # Set the element to False
            b[j] = False
        
        # Increment 'i' by 1
        i += 1
        
        # Update 'j' to the next index, wrapping around with modulo 'n'
        j = (j + i) % n
    
    # Step 5: Create a new list 'x' with elements from 'b' that are still True
    x = [value for value in b if value]
    
    # Step 6: Check the length of 'x'
    if len(x) == 0:
        print('YES')  # All elements were set to False
    else:
        print('NO')   # There are still True elements

# Call the main function
if __name__ == "__main__":
    main()
