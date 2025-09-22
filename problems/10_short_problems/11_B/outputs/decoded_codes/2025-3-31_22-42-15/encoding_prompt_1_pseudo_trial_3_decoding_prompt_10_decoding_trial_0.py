def main():
    # Step 1: Receive input and store the absolute value
    target_value = abs(int(input()))
    
    # Step 2: Initialize the counter
    index = 0
    
    while True:
        # Step 3: Calculate the triangular number
        triangular_number = (index * (index + 1)) // 2
        
        # Step 4: Calculate the difference
        difference = triangular_number - target_value
        
        # Step 5: Check conditions
        if triangular_number == target_value:
            print(index)
            break
        elif triangular_number > target_value:
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 6: Increment the counter
        index += 1

# Call the main function to execute the program
if __name__ == "__main__":
    main()
