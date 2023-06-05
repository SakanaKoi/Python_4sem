n = 12
print(n % sum(int(digit) for digit in str(n)) == 0)