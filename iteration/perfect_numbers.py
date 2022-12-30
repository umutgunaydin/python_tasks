"""
Write a function named perfect_numbers which takes an integer N and returns a tuple containing three lists. The first list contains "perfect" numbers, the second list contains a list of "deficient" numbers, and the third list contains a list of "abundant" numbers.

A number is "perfect" if it is equal to the sum of its proper divisors.
A number is "deficient" if it is less than the sum of its proper divisors.
A number is "abundant" if it is greater than the sum of its proper divisors.
"""


def perfect_numbers(n):
    perfect = []
    deficient = []
    abundant = []

    for i in range(1, n):
        if sum_of_proper_divisors(i) == i:
            perfect.append(i)
        elif sum_of_proper_divisors(i) < i:
            abundant.append(i)
        elif sum_of_proper_divisors(i) > i:
            deficient.append(i)

    return (perfect, deficient, abundant)


def sum_of_proper_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


print(perfect_numbers(5))
print(perfect_numbers(20))
