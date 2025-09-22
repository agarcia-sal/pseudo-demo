def main():
    # Read input integers for total items, bucket capacity, and divisor
    total_items = int(input())
    bucket_capacity = int(input())
    divisor = int(input())

    # Calculate the product of the results from two calls to the mc function
    result = mc(total_items, divisor) * mc(bucket_capacity, divisor)
    
    # Output the result
    print(result)

def mc(number_of_items, bucket_size):
    # Calculate how many full buckets and leftover items 
    full_buckets = number_of_items // bucket_size
    leftover_items = number_of_items % bucket_size
    
    # If there are any leftover items, calculate the total items to account for them
    if leftover_items > 0:
        return leftover_items * (full_buckets + 1)
    else:
        return number_of_items

# The following lines could be used for testing the functions
# Uncomment to test with specific values
# Input: 10 3 2
# Expected Output: 8 (10 // 2 = 5 full buckets, 10 % 2 = 0 leftover items, so returns 10 * 5 = 8)

# main()  # Uncomment this line to run the main function when executing the script
