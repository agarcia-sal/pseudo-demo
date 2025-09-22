def find_index_for_sum():
    # Step 2: Get input from the user and convert to absolute integer
    input_number = abs(int(input()))
    
    # Step 3: Initialize counter variable
    index = 0
    
    # Step 4: Start an infinite loop
    while True:
        # Step 4.1: Calculate the sum of integers from 0 to index
        sum_of_integers = (index * (index + 1)) // 2
        
        # Step 4.2: Calculate the difference
        difference = sum_of_integers - input_number
        
        # Step 4.3: Check if sum_of_integers equals input_number
        if sum_of_integers == input_number:
            print(index)
            break
        
        # Step 4.4: Check if sum_of_integers is greater than input_number
        elif sum_of_integers > input_number:
            # Step 4.4.1: Check if difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 4.5: Increment index by 1
        index += 1

# Call the function to execute the program
find_index_for_sum()
