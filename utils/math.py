def factors(n):
    result = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.add(i)
            result.add(n // i)
        i += 1
    return sorted(result)
