def find_natural_number():
    # Step 2: Get the absolute value of user input as an integer
    n = abs(int(input()))
    
    # Step 3: Initialize i to 0
    i = 0
    
    # Step 4: Enter an infinite loop
    while True:
        # Step 4.1: Calculate the sum s of the first i natural numbers
        s = i * (i + 1) // 2  # Using integer division for sum
        
        # Step 4.2: Calculate the difference m between s and n
        m = s - n
        
        # Step 4.3: Check if s is equal to n
        if s == n:
            print(i)
            break
        
        # Step 4.4: Check if s is greater than n
        if s > n:
            # Step 4.4.1: Check if m is even
            if m % 2 == 0:
                print(i)
                break
                
        # Step 4.5: Increment i by 1
        i += 1

# Call the function to execute the program
find_natural_number()
