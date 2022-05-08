def power(x, n):
    if n == 0:
        return 1
    small_power = power(x, n // 2)
    if n % 2 == 0:
        return small_power * small_power
    else:
        return x * small_power * small_power


print(power(9, 2))
