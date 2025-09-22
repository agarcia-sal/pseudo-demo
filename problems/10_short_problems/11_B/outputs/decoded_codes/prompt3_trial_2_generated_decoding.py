def main():
    # Step 1: Obtain an absolute integer value from user input
    user_input = abs(int(input()))
    
    # Step 2: Initialize a counter variable
    counter = 0
    
    # Step 3: Continuously process until a break condition is met
    while True:
        # Step 4: Calculate the sum of the first 'counter' numbers
        total_sum = (counter * (counter + 1)) // 2
        
        # Step 5: Calculate the difference between the sum and the user input
        difference = total_sum - user_input
        
        # Step 6: Check if the sum equals the user input
        if total_sum == user_input:
            print(counter)   # Output the current counter value
            break            # Exit the loop
        
        # Step 7: Check if the sum is greater than the user input
        elif total_sum > user_input:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:
                print(counter)   # Output the current counter value
                break            # Exit the loop
        
        # Step 9: Increment the counter for the next iteration
        counter += 1

# Invoke the main function to execute the program
main()
