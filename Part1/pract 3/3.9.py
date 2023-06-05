def fast_mul_gen(x):
    s = 'def fast_mul(x):\n'
    s += '    r = 0\n'
    while x > 1:
        if x & 1:
            s += '    r += x\n'
        s += '    x += x\n'
        x >>= 1
    s += '    r += x\n'
    s += '    return r'
    return s

print(fast_mul_gen(12))

def srt(x, y):
    func = fast_mul_gen(y)
    exec(func, globals())
    assert fast_mul(x) == x * y
srt(10, 15)
