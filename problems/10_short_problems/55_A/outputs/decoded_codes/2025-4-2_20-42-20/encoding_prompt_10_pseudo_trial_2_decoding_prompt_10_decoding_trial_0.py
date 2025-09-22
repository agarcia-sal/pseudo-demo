def main():
    # Step 2: Get an integer n from the user
    n = int(input())
    
    # Step 3: Initialize an array b of size n with all values set to True
    b = [True] * n
    
    # Step 4: Initialize variables
    j = 0  # Index for the array
    i = 1  # Step counter
    
    # Step 5: While loop that runs until i exceeds 500000
    while i <= 500000:
        # Step 5a: Check if the current index is True
        if b[j]:
            # Set the value at index j to False
            b[j] = False
            
        # Step 5b: Increment the step counter
        i += 1
        
        # Step 5c: Update index j with wrap-around using modulo
        j = (j + i) % n
    
    # Step 6: Gather elements from b that are still True
    x = [value for value in b if value]
    
    # Step 7: Output result based on the size of x
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# This calls the main function to execute the program
if __name__ == "__main__":
    main()
