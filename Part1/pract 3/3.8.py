def mul16k(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    
    n = max(len(str(x)),len(str(y)))
    halfN = n // 2

    x1 = x // 10**(halfN)
    x0 = x % 10**(halfN)
    y1 = y // 10**(halfN)
    y0 = y % 10**(halfN)

    z0 = mul16k(x0, y0)
    z2 = mul16k(x1, y1)
    z1 = mul16k((x0 + x1), (y0 + y1)) - z0 - z2

    return (z2 * 10**(halfN*2)) + (z1 * 10**halfN) + z0

print(mul16k(int(input()), int(input())))
