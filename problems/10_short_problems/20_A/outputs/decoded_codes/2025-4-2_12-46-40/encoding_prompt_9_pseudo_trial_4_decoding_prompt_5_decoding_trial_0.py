def normalize_path(input_path):
    # Split the input path by the forward slash and filter out empty components
    components = filter(None, input_path.split('/'))
    # Join the components with a single forward slash
    normalized_path = '/' + '/'.join(components)
    return normalized_path

# Start Program
# Step 1: Read entire file path input
file_path = input()

# Step 2: Normalize the file path
normalized_path = normalize_path(file_path)

# Step 3: Ensure that the normalized path starts with a single forward slash
if normalized_path.startswith('//'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 4: Output the final normalized path
print(normalized_path)

# Test cases in comments for edge cases:
# 1. Input: "///usr//bin///python//"
# 2. Input: "/usr/bin/../../etc/../.."
# 3. Input: ""
# 4. Input: "usr/bin"
