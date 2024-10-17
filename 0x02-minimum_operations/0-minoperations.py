def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

# Example testing cases
if _name_ == "_main_":
    print("Min number of operations to reach {} characters: {}".format(4, minOperations(4)))
    print("Min number of operations to reach {} characters: {}".format(12, minOperations(12)))
    print("Min number of operations to reach {} characters: {}".format(9, minOperations(9)))
