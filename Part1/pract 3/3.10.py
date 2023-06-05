def fast_pow_gen(x):
    s = 'def fast_pow(x):\n'
    s += '    r = 1\n'
    while x > 1:
        if x & 1:
            s += '    r *= x\n'
        s += '    x *= x\n'
        x >>= 1
    s += '    r *= x\n'
    s += '    return r\n'
    return s
print(fast_pow_gen(10))

def srt(x, y):
    func = fast_pow_gen(y)
    exec(func, globals())
    assert fast_pow(x) == x ** y
srt(10, 15)
