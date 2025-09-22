# Input Read
total_items = int(input())
additional_items = int(input())
group_size = int(input())

# Define Function mc
def mc(total_items, group_size):
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    if remainder > 0:
        return remainder * (1 + complete_groups)
    else:
        return total_items

# Main Calculation
result_n = mc(total_items, group_size)
result_m = mc(additional_items, group_size)
final_result = result_n * result_m

# Output
print(final_result)
