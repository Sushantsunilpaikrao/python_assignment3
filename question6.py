def powers_of_two(exponent):
    for i in range(exponent + 1):
        yield 2 ** i

exponent = 5
for power in powers_of_two(exponent):
    print(power)
