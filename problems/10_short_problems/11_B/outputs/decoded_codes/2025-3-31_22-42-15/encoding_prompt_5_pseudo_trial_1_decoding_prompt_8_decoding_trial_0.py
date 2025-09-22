# Function to find the index based on the input value
def find_index():
    # Step 1: Accept an input value
    inputValue = abs(int(input()))
    index = 0
    
    # Step 2: Start an infinite loop to find the correct index
    while True:
        # Step 3: Calculate the sum of the first 'index' natural numbers
        sum_value = (index * (index + 1)) // 2
        
        # Step 4: Calculate the difference between the sum and input value
        difference = sum_value - inputValue
        
        # Step 5: Check if the sum equals the input value
        if sum_value == inputValue:
            # Step 5a: Print the current index
            print(index)
            break
        
        # Step 6: Check if the sum is greater than the input value
        elif sum_value > inputValue:
            # Step 6a: Check if the difference is even
            if difference % 2 == 0:
                # Step 6b: Print the current index
                print(index)
                break
        
        # Step 7: Move to the next index for the next iteration
        index += 1

# Example usage
find_index()
