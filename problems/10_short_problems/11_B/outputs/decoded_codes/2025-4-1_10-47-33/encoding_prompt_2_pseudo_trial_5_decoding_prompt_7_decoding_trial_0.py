# Function to determine the smallest integer based on given criteria
def find_smallest_integer():
    # 1. Receive an integer input and compute its absolute value
    absoluteValue = abs(int(input()))
    
    # 2. Initialize index variable
    index = 0

    # 3. Start infinite loop to evaluate conditions based on index
    while True:
        # Calculate the sum of the first 'index' integers using the formula
        sumOfIntegers = (index * (index + 1)) // 2
        
        # Calculate the difference between sumOfIntegers and absoluteValue
        difference = sumOfIntegers - absoluteValue
        
        # 4. Check if sumOfIntegers equals absoluteValue
        if sumOfIntegers == absoluteValue:
            print(index)  # Print the index as the result
            break  # Exit the loop
        
        # 5. Check if sumOfIntegers is greater than absoluteValue
        if sumOfIntegers > absoluteValue:
            # 6. Check if difference is an even number
            if difference % 2 == 0:
                print(index)  # Print the index as the result
                break  # Exit the loop
        
        # Increment index to evaluate the next integer
        index += 1

# Execute the function when the script is run
if __name__ == "__main__":
    find_smallest_integer()
