def main():
    # Step 1: Get user input and ensure it is a non-negative integer
    user_input = abs(int(input()))
    counter = 0

    # Step 2: Start an infinite loop to iterate through possible values
    while True:
        # Step 3: Calculate the current triangular number
        current_triangular_number = (counter * (counter + 1)) // 2
        
        # Step 4: Determine the difference between the triangular number and user input
        difference = current_triangular_number - user_input
        
        # Step 5: Check conditions to decide what to do next
        if current_triangular_number == user_input:
            # If the triangular number equals user input, print the counter and stop
            print(counter)
            break
        elif current_triangular_number > user_input:
            # If the triangular number exceeds user input, check if difference is even
            if difference % 2 == 0:
                # If the difference is even, print the counter and stop
                print(counter)
                break

        # Step 6: Increment the counter for the next iteration
        counter += 1

# Running the main function
if __name__ == '__main__':
    main()
