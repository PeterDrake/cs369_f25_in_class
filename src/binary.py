def int_to_bit(n):
    result = ""
    while n >= 1:
        result = str(n % 2) + result
        n //= 2
    return result

print([int_to_bit(n) for n in [8, 5, 3, 16]])
# print(int_to_bit(8), int_to_bit(5), int_to_bit(3), int_to_bit(16))