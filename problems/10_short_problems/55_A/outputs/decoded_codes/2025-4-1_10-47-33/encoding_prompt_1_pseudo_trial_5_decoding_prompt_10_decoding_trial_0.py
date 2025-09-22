def process_elements():
    # Step 1: Input the integer value representing the number of elements (n)
    n = int(input())
    
    # Step 2: Initialize a list (b) of size n with all values set to True
    b = [True] * n
    
    # Step 3: Set index variable j to 0
    j = 0
    
    # Step 4: Set counter variable i to 1
    counter = 1
    
    # Step 5: While counter is less than or equal to 500000
    while counter <= 500000:
        # Step 5.1: If the value at index j in list b is True
        if b[j]:
            # Step 5.2: Set the value at index j in list b to False
            b[j] = False
        
        # Step 5.3: Increment the counter variable i by 1
        counter += 1
        
        # Step 5.4: Update the index j to be the remainder of (j + i) divided by n
        j = (j + counter) % n
    
    # Step 6: Create a new list (x) that contains all values from list b that are still True
    x = [value for value in b if value]
    
    # Step 7: If the length of list x is equal to 0
    if len(x) == 0:
        # Output "YES"
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Call the function to execute the code
process_elements()
