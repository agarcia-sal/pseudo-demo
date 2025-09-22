# Step 1: Start the program (not explicitly coded in Python)

# Step 2: Read an integer input value and store its absolute value in a variable `number`
number = abs(int(input()))

# Step 3: Initialize a counter variable `index` to 0
index = 0

# Step 4: Begin an infinite loop
while True:
    # Step 4a: Calculate the sum of the first `index` natural numbers
    sum_of_first_index = (index * (index + 1)) / 2
    
    # Step 4b: Calculate the difference between `sum_of_first_index` and `number`
    difference = sum_of_first_index - number
    
    # Step 4c: Check if `sum_of_first_index` is equal to `number`
    if sum_of_first_index == number:
        print(index)
        break  # exit the loop
    
    # Step 4d: Else, check if `sum_of_first_index` is greater than `number`
    elif sum_of_first_index > number:
        # Step 4d: Check if `difference` is even
        if difference % 2 == 0:
            print(index)
            break  # exit the loop
    
    # Step 4e: Increment `index` by 1
    index += 1

# Step 5: End the program (not explicitly coded in Python)
