def get_discounted_price(price):
    return price

def calculate_tax(price):
    return price * 0.18

def checkout(price):
    discounted = get_discounted_price(price)
    tax = calculate_tax(price)
    return discounted + tax
