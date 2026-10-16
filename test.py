
TAX_RATE = 0.20


def calculate_tax(amount):
    return amount * TAX_RATE


def main():
    amount = 1000
    print("Tax:", calculate_tax(amount))


if __name__ == "__main__":
    main()
