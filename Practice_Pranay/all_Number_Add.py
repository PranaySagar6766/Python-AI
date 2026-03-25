def sum_of_digits(n):
    return sum(int (d) for d in str(abs(n)))

print(sum_of_digits(304888344611713860501504000000))