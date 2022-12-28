# Write a recursive function named fibonacci_series that takes an integer, N, as argument
# and returns the first N numbers of the Fibonacci series.
def fibonacci_series(n):
    if n <= 1:
        return [0]
    elif n == 2:
        return [0, 1]
    series = fibonacci_series(n - 1)

    return series + [series[-2] + series[-1]]


print(fibonacci_series(11))
