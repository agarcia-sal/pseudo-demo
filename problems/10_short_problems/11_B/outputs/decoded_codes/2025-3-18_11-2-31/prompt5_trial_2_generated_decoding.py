# Function to find the triangular number counter based on input conditions
def find_triangular_number_counter():
    # Step 1: Read an integer input and convert it to its absolute value
    input_number = abs(int(input()))

    # Step 2: Initialize a counter
    counter = 0

    # Step 3: Begin an infinite loop to find the desired integer
    while True:
        # Step 4: Calculate the triangular number using the formula
        triangular_number = (counter * (counter + 1)) // 2
        
        # Step 5: Calculate the difference between the triangular number and the input number
        difference = triangular_number - input_number
        
        # Step 6: Check if the triangular number equals the input number
        if triangular_number == input_number:
            # Step 7: Print the counter when conditions are satisfied
            print(counter)
            break  # Exit the loop
        
        # Step 8: Check if the triangular number is greater than the input number
        elif triangular_number > input_number:
            # Step 9: Check if the difference is even
            if difference % 2 == 0:
                # Step 10: Print the counter when conditions are satisfied
                print(counter)
                break  # Exit the loop
        
        # Step 11: Increment the counter for the next iteration
        counter += 1

# Uncomment the line below to run the function
# find_triangular_number_counter()
