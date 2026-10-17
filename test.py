
TAX_RATE = 0.10


def calculate_discounted_price(price):
    discount = price * 0.20
    return price - discount


def checkout(price):
    discounted_price = calculate_discounted_price(price)
    tax = discounted_price * TAX_RATE
    return discounted_price + tax


def main():
    print("Final price:", checkout(1000))


if __name__ == "__main__":
    main()
