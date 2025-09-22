def main():
    # Read input integers for total items and bucket capacity
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

# Calling the main function to execute the program
main()
