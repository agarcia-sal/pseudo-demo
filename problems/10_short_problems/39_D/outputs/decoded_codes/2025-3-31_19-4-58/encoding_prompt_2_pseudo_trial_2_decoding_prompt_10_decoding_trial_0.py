def main():
    # Step 2: Receive Input
    first_input = input()
    second_input = input()
    
    # Step 3: Process Input
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Step 4: Initialize count variable
    discrepancy_count = 0
    
    # Step 5: Comparison Loop
    for index in range(3):  # Loop through first three elements
        value_from_first = int(first_values[index])
        value_from_second = int(second_values[index])
        
        if value_from_first != value_from_second:
            discrepancy_count += 1
    
    # Step 6: Final Decision
    if discrepancy_count < 3:
        print("YES")
    else:
        print("NO")
        
# Step 1: Start the main procedure
if __name__ == "__main__":
    main()
