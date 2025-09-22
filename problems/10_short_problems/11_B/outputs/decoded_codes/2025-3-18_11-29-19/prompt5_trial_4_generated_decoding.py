# Function to find the index of the triangular number or the required condition
def find_triangular_index():
    # Step 1: Get input from the user and convert it to a non-negative integer
    user_input = abs(int(input()))
    
    # Step 2: Initialize a counter variable to track the current triangular number index
    index = 0
    
    # Step 3: Create an infinite loop to search for the desired index
    while True:
        # Step 4: Calculate the current triangular number
        triangular_number = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference between the triangular number and user input
        difference = triangular_number - user_input
        
        # Step 6: Check if the triangular number is equal to the user input
        if triangular_number == user_input:
            # Step 6a: Print the found index and exit the loop
            print(index)
            break
        
        # Step 7: Check if the triangular number exceeds the user input
        elif triangular_number > user_input:
            # Step 7a: Check if the difference is even
            if difference % 2 == 0:
                # Step 7b: Print the index since the difference is even and exit the loop
                print(index)
                break
        
        # Step 8: Increment the index to check the next triangular number in the next iteration
        index += 1

# Call the function to execute the program
find_triangular_index()
