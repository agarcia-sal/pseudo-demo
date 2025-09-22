def main():
    # Step 1: Read integer input for totalCount
    total_count = int(input())
    
    # Step 2: Create a boolean array of size totalCount, initialized to True
    boolean_array = [True] * total_count
    
    # Step 3: Initialize incrementValue and index
    increment_value = 1
    index = 0
    
    # Step 4: Loop while incrementValue is less than or equal to 500,000
    while increment_value <= 500000:
        # Check if the current index in boolean_array is True
        if boolean_array[index]:
            # Change value at current index to False
            boolean_array[index] = False
        
        # Update incrementValue and index
        increment_value += 1
        index = (index + increment_value) % total_count  # Ensure it wraps using modulus

    # Step 5: Create a list of indices where the value is still True
    true_values = [i for i, value in enumerate(boolean_array) if value]
    
    # Step 6: Check if trueValues is empty and print the result
    if len(true_values) == 0:
        print("YES")
    else:
        print("NO")

# Entry point of the script
if __name__ == "__main__":
    main()
