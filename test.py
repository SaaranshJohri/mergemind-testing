
def calculate_discount(price):
    return price * 0.15


def calculate_shipping(weight):
    return weight * 5


def main():
    price = 1000
    weight = 2

    print("Discount:", calculate_discount(price))
    print("Shipping:", calculate_shipping(weight))


if __name__ == "__main__":
    main()
