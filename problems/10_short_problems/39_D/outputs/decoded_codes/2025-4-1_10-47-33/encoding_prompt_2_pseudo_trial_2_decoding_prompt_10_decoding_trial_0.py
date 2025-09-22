def main():
    # Step 2: Receive input
    first_input = input()
    second_input = input()

    # Step 3: Process the inputs
    first_list = first_input.split()
    second_list = second_input.split()
    
    difference_count = 0  # Initialize a counter for differing elements

    # Step 4: Compare elements
    for index in range(3):  # Loop through the first three elements
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer
        
        if first_number != second_number:  # Check for differences
            difference_count += 1  # Increment count if numbers differ

    # Step 5: Evaluate the results
    if difference_count < 3:  # If fewer than 3 differences
        print("YES")
    else:  # If 3 or more differences
        print("NO")

if __name__ == "__main__":
    main()  # Start the program


   1 2 3
   1 2 3
   

   1 2 3
   4 2 3
   

   1 2 3
   4 5 6
   

   1 0 0
   1 1 0
   