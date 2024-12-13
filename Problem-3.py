def gen_series(a):
    if a % 2 == 0:
        a -= 1
    series = [2 * i - 1 for i in range(1,a + 1)]
    return ", ".join(map(str, series))

a = int(input("Enter a positive integer: "))
print(gen_series(a))
