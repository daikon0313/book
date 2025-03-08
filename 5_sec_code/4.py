# numbers = [20, 15, 10, 5]
# numbers.sort()
# print(numbers)

# numbers = [20, 15, 10, 5]
# numbers_asc = sorted(numbers)
# print(f"numbers: {numbers}")
# print(f"numbers_asc: {numbers_asc}")

# prices = [1000, 2000]

# def total_price(price):
#     """送料500"""
#     prices.append(500)
#     total = sum(prices)
#     print(f"{total}円")

# total_price(prices)
# total_price(prices)
# total_price(prices)

# prices = [1000, 2000]

# def total_price(prices):
#     """送料500"""
#     prices = prices + [500]
#     total = sum(prices)
#     print(f"{total}円")

# total_price(prices)
# total_price(prices)
# total_price(prices)

import random
import timeit

x = [random.random() for _ in range(1000)]
#
print(timeit.timeit(lambda: x.sort()))
print(timeit.timeit(lambda: sorted(x)))