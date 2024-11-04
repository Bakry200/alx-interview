def validUTF8(data):
    def check(byte):
        return (byte & 0xC0) == 0x80

    n_bytes = 0

    for byte in data:
        byte &= 0xFF  # Only keep the last 8 bits

        if n_bytes == 0:
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if not check(byte):
                return False
            n_bytes -= 1

    return n_bytes == 0

# Example testing cases
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # Should return True
    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # Should return True
    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Should return False
