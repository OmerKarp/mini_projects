import math

a = 0
b = 2 * math.pi


def approximation(t):
    real_int = 7.9549265
    approx_int = 0
    temp_sum = 0
    temp_value = 0
    for i in range(1, t):
        temp_value = math.e ** math.sin(((b - a) / t) * i)
        temp_sum += temp_value
    approx_int = ((b - a) / t) * (1 + temp_sum)
    print(f"""for {t} intervals:absolute error: {abs(real_int - approx_int)} relative error: {abs(real_int - approx_int) / real_int}""")


for interval in range(1, 21):
    approximation(interval)


