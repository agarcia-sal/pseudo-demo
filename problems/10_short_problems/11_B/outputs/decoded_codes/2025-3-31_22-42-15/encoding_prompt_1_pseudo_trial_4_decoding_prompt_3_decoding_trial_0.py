def find_index():
    # Step 1: Start the program
    # Step 2: Read an integer input value and store its absolute value in a variable `number`
    number = abs(int(input()))
    
    # Step 3: Initialize a counter variable `index` to 0
    index = 0

    # Step 4: Begin an infinite loop
    while True:
        # Step 4a: Calculate the sum of the first `index` natural numbers
        sum_of_first_index = (index * (index + 1)) // 2
        
        # Step 4b: Calculate the difference between `sum_of_first_index` and `number`
        difference = sum_of_first_index - number
        
        # Step 4c: Check if `sum_of_first_index` is equal to `number`
        if sum_of_first_index == number:
            print(index)  # If true, print the value of `index` and exit the loop
            break
        
        # Step 4d: Else, check if `sum_of_first_index` is greater than `number`
        if sum_of_first_index > number:
            # If true, check if `difference` is even
            if difference % 2 == 0:
                print(index)  # If true, print the value of `index` and exit the loop
                break
        
        # Step 4e: Increment `index` by 1
        index += 1

# Call the function to execute the program
find_index()
