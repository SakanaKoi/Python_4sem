#3.7
def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y
def mul16(x, y):
    xF8 = (x >> 8)
    yF8 = (y >> 8)
    return (mul_bits(xF8, yF8, 8) << 16) + ((mul_bits(xF8, y, 8) + mul_bits(x, yF8, 8)) << 8) + mul_bits(x, y,8)
print(mul16(64000, 65000))
print(64000 * 65000)
