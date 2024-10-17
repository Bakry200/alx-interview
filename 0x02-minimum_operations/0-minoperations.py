def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    buffer = 0

    while current_length < n:
        if n % current_length == 0:
            buffer = current_length
            operations += 1  # Copy All
        current_length += buffer
        operations += 1  # Paste

    return operations

# Example usage
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
    n = 12
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
