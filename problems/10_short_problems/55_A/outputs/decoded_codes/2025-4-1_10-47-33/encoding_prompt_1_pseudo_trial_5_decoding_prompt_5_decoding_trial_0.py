def check_elements_status():
    # Input the number of elements
    n = int(input())
    
    # Initialize a list of size n with all values set to True
    b = [True] * n
    
    # Set index variable j to 0
    j = 0
    
    # Set counter variable i to 1
    i = 1
    
    # Loop while i is less than or equal to 500000
    while i <= 500000:
        # If the value at index j in list b is True
        if b[j]:
            # Set the value at index j in list b to False
            b[j] = False
        
        # Increment the counter variable i by 1
        i += 1
        
        # Update the index j to be the remainder of (j + i) divided by n
        j = (j + i) % n
    
    # Create a new list that contains all values from list b that are still True
    x = [value for value in b if value]
    
    # If the length of list x is equal to 0
    if len(x) == 0:
        # Output "YES"
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Example test cases
# check_elements_status()  # Uncomment to test the function
