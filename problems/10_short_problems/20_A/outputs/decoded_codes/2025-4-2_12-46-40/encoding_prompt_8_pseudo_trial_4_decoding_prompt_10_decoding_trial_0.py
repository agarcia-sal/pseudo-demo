import re

def main():
    # Read the input from standard input and strip any extra whitespace
    input_path = input().strip()
    
    # Normalize the path by replacing multiple leading slashes with a single leading slash
    normalized_path = normalize_path(input_path)
    
    # Print the normalized path to output
    print(normalized_path)

def normalize_path(path):
    # Use a regex to replace multiple leading slashes with a single leading slash
    # This will also handle the case where there are no slashes
    return re.sub(r'(^/)+', '/', path)

# Start execution by calling the main function
if __name__ == "__main__":
    main()
