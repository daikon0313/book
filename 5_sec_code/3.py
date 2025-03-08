# prices = [1000, 2000]

# def total_price():
#     """送料を500円"""
#     prices.append(500)
#     total = sum(prices)
#     print(f"{total}円")

# total_price()
# total_price()
# total_price()

prices = [1000, 2000]

def total_price(prices):
    """送料を500円"""
    prices = prices.copy()
    prices.append(500)
    total = sum(prices)
    print(f"{total}円")

total_price(prices)
total_price(prices)
total_price(prices)

